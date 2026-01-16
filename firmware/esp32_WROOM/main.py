import time
import ujson
from machine import Pin, PWM
from microdot import Microdot
from microdot.websocket import with_websocket

# ==================================================
# PIN DEFINITIONS
# ==================================================

DIR_FR = Pin(2, Pin.OUT)     # Right front direction
DIR_FL = Pin(4, Pin.OUT)     # Left front direction
DIR_BR = Pin(5, Pin.OUT)     # Right back direction
DIR_BL = Pin(13, Pin.OUT)    # Left back direction

FR_PWM = PWM(Pin(18), freq=20000)
BR_PWM = PWM(Pin(19), freq=20000)
FL_PWM = PWM(Pin(32), freq=20000)
BL_PWM = PWM(Pin(33), freq=20000)

MOTOR_IN1 = Pin(25, Pin.OUT)
MOTOR_IN2 = Pin(26, Pin.OUT)

servoPin = Pin(12, Pin.OUT)
signalPin = Pin(23, Pin.OUT)

# ==================================================
# CONSTANTS
# ==================================================

TRACK_WIDTH = 0.465
HALF_WIDTH = TRACK_WIDTH / 2

MAX_SPEED = 1.0
MAX_ANG = 1.0
VEL_TO_PWM = 200

POWER_TANK = 120     # strong tank turn power

# ==================================================
# SAFE STARTUP
# ==================================================
def all_stop():
    FR_PWM.duty(0); BR_PWM.duty(0)
    FL_PWM.duty(0); BL_PWM.duty(0)

    DIR_FR.value(0); DIR_BR.value(0)
    DIR_FL.value(0); DIR_BL.value(0)

    MOTOR_IN1.value(0); MOTOR_IN2.value(0)
    servoPin.value(0); signalPin.value(0)

all_stop()

# ==================================================
# HELPERS
# ==================================================
def set_pwm(pwm, val):
    val = max(min(int(val), 255), 0)
    pwm.duty(val)

def clamp(x, lo, hi):
    return max(min(x, hi), lo)

# ==================================================
# VELOCITY → PWM (ARCADE DRIVE)
# ==================================================
def set_velocity(v, w):
    v = clamp(v, -MAX_SPEED, MAX_SPEED)
    w = clamp(w, -MAX_ANG, MAX_ANG)

    Vr = v + w * HALF_WIDTH
    Vl = v - w * HALF_WIDTH

    right_pwm = Vr * VEL_TO_PWM
    left_pwm  = Vl * VEL_TO_PWM

    # -------------------------------
    # RIGHT WHEELS DIRECTION
    # -------------------------------
    if right_pwm >= 0:
        DIR_FR.value(1); DIR_BR.value(1)     # RIGHT forward = DIR=1
    else:
        DIR_FR.value(0); DIR_BR.value(0)     # RIGHT reverse = DIR=0

    set_pwm(FR_PWM, abs(right_pwm))
    set_pwm(BR_PWM, abs(right_pwm))

    # -------------------------------
    # LEFT WHEELS DIRECTION
    # (your wiring: DIR=0 forward / DIR=1 reverse)
    # -------------------------------
    if left_pwm >= 0:
        DIR_FL.value(0); DIR_BL.value(0)     # LEFT forward
    else:
        DIR_FL.value(1); DIR_BL.value(1)     # LEFT reverse

    set_pwm(FL_PWM, abs(left_pwm))
    set_pwm(BL_PWM, abs(left_pwm))

# ==================================================
# TANK TURN OVERRIDE (D-PAD)
# ==================================================
def tank_left():
    print("TANK LEFT (override)")

    # RIGHT wheels forward
    DIR_FR.value(1); DIR_BR.value(1)
    set_pwm(FR_PWM, POWER_TANK)
    set_pwm(BR_PWM, POWER_TANK)

    # LEFT wheels reverse (DIR=1 = reverse)
    DIR_FL.value(1); DIR_BL.value(1)
    set_pwm(FL_PWM, POWER_TANK)
    set_pwm(BL_PWM, POWER_TANK)

def tank_right():
    print("TANK RIGHT (override)")

    # LEFT wheels forward (DIR=0 = forward)
    DIR_FL.value(0); DIR_BL.value(0)
    set_pwm(FL_PWM, POWER_TANK)
    set_pwm(BL_PWM, POWER_TANK)

    # RIGHT wheels reverse (DIR=0 = reverse)
    DIR_FR.value(0); DIR_BR.value(0)
    set_pwm(FR_PWM, POWER_TANK)
    set_pwm(BR_PWM, POWER_TANK)

def stop_tank():
    print("STOP TANK")
    all_stop()

# ==================================================
# ACTUATOR + DUMP
# ==================================================
def up(): MOTOR_IN1.value(1); MOTOR_IN2.value(0)
def down(): MOTOR_IN1.value(0); MOTOR_IN2.value(1)
def stop_actuator(): MOTOR_IN1.value(0); MOTOR_IN2.value(0)
def dump(): servoPin.value(1)

# ==================================================
# WEBSOCKET SERVER
# ==================================================
app = Microdot()

@app.route("/")
def index(req):
    return "ESP32 Rover Ready"

@app.route("/ws")
@with_websocket
async def ws_handler(req, ws):

    print("WS connected")
    TANK_MODE = False

    try:
        while True:
            msg = await ws.receive()
            if msg is None:
                break

            msg = msg.strip()
            print("RX:", msg)

            # ----------------------------------------
            # TANK OVERRIDE (D-Pad)
            # ----------------------------------------
            if msg == "TANK_LEFT":
                TANK_MODE = True
                tank_left()
                await ws.send("ACK")
                continue

            if msg == "TANK_RIGHT":
                TANK_MODE = True
                tank_right()
                await ws.send("ACK")
                continue

            if msg == "TANK_STOP":
                TANK_MODE = False
                stop_tank()
                await ws.send("ACK")
                continue

            # ----------------------------------------
            # Ignore v/w during tank mode
            # ----------------------------------------
            if TANK_MODE:
                await ws.send("ACK")
                continue

            # ----------------------------------------
            # NORMAL VELOCITY MODE
            # ----------------------------------------
            if msg.startswith("{"):
                try:
                    data = ujson.loads(msg)
                    v = float(data.get("v", 0))
                    w = float(data.get("w", 0))
                    set_velocity(v, w)
                except Exception as e:
                    print("JSON error:", e)

                await ws.send("ACK")
                continue

            # ----------------------------------------
            # ACTUATOR / SIGNAL
            # ----------------------------------------
            if msg == "RB_DOWN":   up()
            elif msg == "RB_UP":   stop_actuator()
            elif msg == "LB_DOWN": down()
            elif msg == "LB_UP":   stop_actuator()
            elif msg == "triangle": dump()
            elif msg == "X":        signalPin.value(1)

            await ws.send("ACK")

    finally:
        all_stop()
        print("WS disconnected")

print("Microdot running on 0.0.0.0:81")
app.run(host="0.0.0.0", port=81)