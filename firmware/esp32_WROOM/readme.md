# ⚡ ESP32 Runtime Files (MicroPython)

This folder represents the **files stored on the ESP32’s internal flash** when running MicroPython. These files are uploaded directly to the board and executed at runtime.

---

## 📄 Files

### 🚀 `boot.py`

* Runs **first** on every power-up or reset
* Handles **safe startup behavior** and **Wi-Fi connection**
* Prevents unintended motor movement during boot

---

### 🤖 `main.py`

* Primary control program
* Implements **linear (`v`) and rotational (`w`) velocity control**
* Uses **differential-drive kinematics**
* Controls motors, actuators, and peripherals
* Communicates via **WebSockets (Microdot)**

---

### 🧪 `test.py` (if present)

* Standalone motor test utility
* Tests each wheel **individually** (forward / reverse)
* Used for wiring, controller, and power debugging
* Not executed automatically

---

## 🛠 Usage Notes

* These files are uploaded using tools such as:

  * `mpremote`
  * Thonny
  * rshell
* Only **one `main.py`** runs automatically at a time
* This folder is **not part of `ros2_ws/src`**

---

## 📌 Rule of Thumb

> **If it runs on the ESP32, it lives here.**


