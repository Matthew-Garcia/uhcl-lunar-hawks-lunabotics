import argparse, time
import websocket
import json
from evdev import InputDevice, ecodes, list_devices

# ============================================================
# CONTROLLER CONSTANTS
# ============================================================

DEADZONE = 0.10
CENTER_Y = None   # forward/back calibration
CENTER_X = None   # left/right calibration

# ============================================================
# CALIBRATION HELPERS
# ============================================================

def calibrate_center_y(raw):
    global CENTER_Y
    if CENTER_Y is None:
        CENTER_Y = raw
        print(f"🎯 Calibrated CENTER_Y = {CENTER_Y}")

def calibrate_center_x(raw):
    global CENTER_X
    if CENTER_X is None:
        CENTER_X = raw
        print(f"🎯 Calibrated CENTER_X = {CENTER_X}")

def apply_deadzone(v):
    return 0.0 if abs(v) < DEADZONE else v

# ============================================================
# WEBSOCKET CONNECTION
# ============================================================

def connect(url):
    while True:
        try:
            print(f"🔗 Connecting to {url} ...")
            ws = websocket.WebSocket()
            ws.connect(url)
            print("✅ WebSocket Connected!")
            return ws
        except Exception as e:
            print("❌ Connection failed:", e)
            time.sleep(1)

def pick_gamepad():
    devices = [InputDevice(p) for p in list_devices()]
    for d in devices:
        if "xbox" in d.name.lower() or "controller" in d.name.lower():
            print(f"🎮 Using: {d.path} – {d.name}")
            return d
    raise RuntimeError("No controller detected!")

# ============================================================
# MAIN LOOP
# ============================================================

def main():
    global CENTER_Y, CENTER_X

    ap = argparse.ArgumentParser()
    ap.add_argument("--ip", required=True)
    ap.add_argument("--port", type=int, default=81)
    args = ap.parse_args()

    url = f"ws://{args.ip}:{args.port}/ws"
    ws = connect(url)
    dev = pick_gamepad()

    print("\n🎮 Controller active…")
    print("👉 Let LEFT stick sit centered for calibration\n")

    try:
        for ev in dev.read_loop():

            # ============================================================
            # LEFT STICK → {"v":..., "w":...}
            # ============================================================
            if ev.type == ecodes.EV_ABS:

                # -------------------- v (forward/back)
                if ev.code == ecodes.ABS_Y:
                    raw = ev.value
                    if CENTER_Y is None:
                        calibrate_center_y(raw)
                        continue

                    norm_v = (raw - CENTER_Y) / 32768.0
                    norm_v = -apply_deadzone(norm_v)

                # -------------------- w (left/right)
                elif ev.code == ecodes.ABS_X:
                    raw = ev.value
                    if CENTER_X is None:
                        calibrate_center_x(raw)
                        continue

                    norm_w = (raw - CENTER_X) / 32768.0
                    norm_w = apply_deadzone(norm_w)

                else:
                    continue

                # Send JSON velocity if calibrated
                if CENTER_Y is not None and CENTER_X is not None:
                    v = norm_v if "norm_v" in locals() else 0.0
                    w = norm_w if "norm_w" in locals() else 0.0

                    msg = json.dumps({"v": v, "w": w})
                    ws.send(msg)
                    print(f"📡 v={v:.2f}   w={w:.2f}")

            # ============================================================
            # D-PAD → TANK TURN OVERRIDE
            # ============================================================
            if ev.type == ecodes.EV_ABS and ev.code == ecodes.ABS_HAT0X:

                hat = ev.value  # -1 = left, 0 = stop, 1 = right

                if hat == -1:
                    ws.send("TANK_LEFT")
                    print("↩️ **TANK LEFT** (override)")

                elif hat == 1:
                    ws.send("TANK_RIGHT")
                    print("↪️ **TANK RIGHT** (override)")

                elif hat == 0:
                    ws.send("TANK_STOP")
                    print("🛑 **STOP TANK** (return to normal mode)")

            # ============================================================
            # BUTTONS → actuator / dump / signal
            # ============================================================
            if ev.type == ecodes.EV_KEY:

                # ---------- PRESSED ----------
                if ev.value == 1:

                    if ev.code == ecodes.BTN_TR:
                        ws.send("RB_DOWN")
                        print("RB → Actuator UP")

                    elif ev.code == ecodes.BTN_TL:
                        ws.send("LB_DOWN")
                        print("LB → Actuator DOWN")

                    elif ev.code == ecodes.BTN_NORTH:
                        ws.send("triangle")
                        print("Y → Dump")

                    elif ev.code == ecodes.BTN_SOUTH:
                        ws.send("X")
                        print("A → Signal HIGH")

                # ---------- RELEASED ----------
                elif ev.value == 0:

                    if ev.code == ecodes.BTN_TR:
                        ws.send("RB_UP")

                    elif ev.code == ecodes.BTN_TL:
                        ws.send("LB_UP")

    except KeyboardInterrupt:
        ws.send(json.dumps({"v": 0, "w": 0}))
        print("\n🛑 STOP sent. Exiting controller...")

# ============================================================
# PROGRAM ENTRY
# ============================================================

if __name__ == "__main__":
    main()

