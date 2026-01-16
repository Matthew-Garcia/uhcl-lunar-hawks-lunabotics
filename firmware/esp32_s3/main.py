# main.py
import math
from machine import Pin, PWM
from microdot import Microdot
from microdot.websocket import with_websocket

# ---- Rover params ----
L = 0.25          # wheelbase (m)
MAX_SPEED = 1.0   # max linear speed (m/s)

# ---- LEFT motor (valid pins) ----
L_IN1 = Pin(12, Pin.OUT)
L_IN2 = Pin(13, Pin.OUT)
L_PWM = PWM(Pin(14), freq=1000)

# ---- RIGHT motor (valid pins) ----
R_IN1 = Pin(19, Pin.OUT)
R_IN2 = Pin(20, Pin.OUT)
R_PWM = PWM(Pin(18), freq=1000)

def _clip01(x): return 0 if x < 0 else (1 if x > 1 else x)

def set_motor(side: str, speed: float):
    # speed in m/s, signed
    direction = 1 if speed >= 0 else -1
    duty = int(_clip01(abs(speed) / MAX_SPEED) * 1023)

    if side == 'L':
        L_IN1.value(1 if direction > 0 else 0)
        L_IN2.value(0 if direction > 0 else 1)
        L_PWM.duty(duty)
    else:
        R_IN1.value(1 if direction > 0 else 0)
        R_IN2.value(0 if direction > 0 else 1)
        R_PWM.duty(duty)

def stop_motors():
    for p in (L_PWM, R_PWM):
        p.duty(0)
    for p in (L_IN1, L_IN2, R_IN1, R_IN2):
        p.value(0)

app = Microdot()

@app.route('/')
def index(req):
    return 'ESP32 Rover WebSocket online (use /ws)'

@app.route('/ws')
@with_websocket
async def ws_handler(req, ws):
    print("WS client connected")
    try:
        while True:
            msg = await ws.receive()     # <-- await here
            if msg is None:
                break
            msg = msg.strip()
            print("RX:", msg)

            if msg.startswith('v,'):
                try:
                    _, v_str, w_str = msg.split(',')
                    v = float(v_str); w = float(w_str)
                except:
                    await ws.send('ERR,bad_format')   # <-- await send
                    continue

                v_l = v - (w * L / 2.0)
                v_r = v + (w * L / 2.0)
                set_motor('L', v_l)
                set_motor('R', v_r)
                await ws.send('ACK')                  # <-- await send
            elif msg.lower() == 'stop':
                stop_motors()
                await ws.send('ACK')
            else:
                await ws.send('ERR,unknown_cmd')
    finally:
        stop_motors()
        print("WS client disconnected")


print("Microdot running on 0.0.0.0:81")
app.run(host='0.0.0.0', port=81)
