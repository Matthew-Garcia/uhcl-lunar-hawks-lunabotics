# ⚡ `flash/` – ESP32 Runtime Files (MicroPython)

This directory represents the files stored on the **ESP32’s internal flash** when running **MicroPython**. These files are uploaded directly to the board and executed on boot.

---

## 📄 Files

### 🚀 `boot.py`

* Runs **first** on every power-up or reset
* Handles **safe startup behavior** and **Wi-Fi connection**
* Ensures motors are in a safe state before `main.py` runs

---

### 🤖 `main.py`

* Primary rover control program
* Handles:

  * Linear (`v`) and rotational (`w`) velocity commands
  * Differential drive motor control
  * Tank turn override (D-pad)
  * Actuator and servo control
  * WebSocket communication via Microdot

---

### 🧪 `test.py`

* Standalone motor test utility
* Tests each wheel’s **direction and PWM output**
* Useful for debugging wiring, motor controllers, or power issues
* Not run automatically unless explicitly executed

---

## 🛠 Notes

* Files in this directory **do not belong in `ros2_ws/src`**
* Uploaded to the ESP32 using tools such as:

  * `mpremote`
  * Thonny
  * rshell
* Only one `main.py` runs automatically at a time

---

## 📌 Quick Rule

> **If it runs on the ESP32, it lives in `flash/`.**
