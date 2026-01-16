# `test.py` – Wheel & Motor Test Utility

This script is used to **individually test each rover wheel** to verify motor wiring, direction control, and PWM behavior **independent of the main rover control code**.

---

## Purpose

* Confirms each wheel can spin **forward and reverse**
* Verifies **direction pin logic** for each motor
* Helps diagnose **wiring, motor controller, or power issues**
* Useful for isolating hardware problems from software issues

---

## How It Works

* Uses the **same pin definitions as `main.py`**
* Forces a **safe startup** (all motors OFF)
* Tests each wheel sequentially:

  1. Spin forward
  2. Stop
  3. Spin reverse
  4. Stop
* Ensures all motors are stopped on exit, even if interrupted

---

## Usage Notes

* Run this script **with the rover lifted off the ground**
* Adjust the `fwd_dir` parameter if a wheel’s forward direction is inverted
* PWM duty is fixed for testing and does not reflect final drive tuning

---

## When to Use

* After wiring changes
* When diagnosing uneven motor behavior
* Before running full rover control software


If you want a **one-paragraph ultra-minimal version** for GitHub, I can compress this further.

