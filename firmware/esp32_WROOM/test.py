import time
from machine import Pin, PWM

# ==================================================
# SAME PIN DEFINITIONS AS MAIN
# ==================================================
DIR_FR = Pin(2, Pin.OUT)
DIR_FL = Pin(4, Pin.OUT)
DIR_BR = Pin(5, Pin.OUT)
DIR_BL = Pin(13, Pin.OUT)

FR_PWM = PWM(Pin(18), freq=20000)
BR_PWM = PWM(Pin(19), freq=20000)
FL_PWM = PWM(Pin(32), freq=20000)
BL_PWM = PWM(Pin(33), freq=20000)

def all_stop():
    FR_PWM.duty(0)
    BR_PWM.duty(0)
    FL_PWM.duty(0)
    BL_PWM.duty(0)

    DIR_FR.value(0)
    DIR_FL.value(0)
    DIR_BR.value(0)
    DIR_BL.value(0)

all_stop()
print("SAFE STARTUP: Motors OFF")

def test_wheel(name, dir_pin, pwm, fwd_dir, duty=180):
    """
    name:   label to print (e.g., 'FR', 'FL')
    dir_pin: the DIR_* Pin object for that wheel
    pwm:    PWM object for that wheel
    fwd_dir: 1 or 0 for 'forward' direction for this wheel
    duty:  PWM duty for the test
    """

    print("\n==============================")
    print("TESTING WHEEL:", name)
    print("==============================")

    # Forward
    print(" -> FORWARD (dir = {})".format(fwd_dir))
    dir_pin.value(fwd_dir)
    pwm.duty(duty)
    time.sleep(2)

    # Stop
    pwm.duty(0)
    time.sleep(1)

    # Reverse
    rev_dir = 0 if fwd_dir == 1 else 1
    print(" -> REVERSE (dir = {})".format(rev_dir))
    dir_pin.value(rev_dir)
    pwm.duty(duty)
    time.sleep(2)

    # Stop
    pwm.duty(0)
    dir_pin.value(0)
    time.sleep(1)
    print("Done with", name)

# ==================================================
# RUN TESTS
# ==================================================
try:
    # You can adjust fwd_dir values if you already know which way is forward.
    # For now we’ll assume:
    #   1 = forward, 0 = reverse  (just for testing)
    test_wheel("FR (Front Right)", DIR_FR, FR_PWM, fwd_dir=1)
    test_wheel("BR (Back Right)",  DIR_BR, BR_PWM, fwd_dir=1)
    test_wheel("FL (Front Left)",  DIR_FL, FL_PWM, fwd_dir=1)
    test_wheel("BL (Back Left)",   DIR_BL, BL_PWM, fwd_dir=1)

finally:
    all_stop()
    print("\nALL STOP. Wheel test complete.")
