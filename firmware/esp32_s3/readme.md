# 🧪 ESP32-S3 Firmware (Non-Rover)

This directory contains **MicroPython runtime files for the ESP32-S3**, used for **non-rover / earlier development and testing** prior to the full Lunabotics rover system.

The ESP32-S3 was used to validate **WebSocket communication** and **linear (`v`) / rotational (`w`) velocity control** in a simplified differential-drive setup.

---

## 📁 Directory Structure

```
esp32_s3/
└── flash/
    ├── boot.py
    └── main.py
```

---

## 📄 Files

### 🚀 `boot.py`

* Executes on power-up or reset
* Connects the ESP32-S3 to the configured Wi-Fi network

---

### 🤖 `main.py`

* WebSocket-based control program
* Accepts **linear (`v`) and rotational (`w`) velocity commands**
* Implements **differential-drive kinematics**
* Converts velocity commands to left/right motor PWM
* Includes safe motor stop handling on disconnect

---

## 🛠 Usage Notes

* Files are uploaded to the ESP32-S3 using:

  * `mpremote`
  * Thonny
  * rshell
* MicroPython firmware must be flashed **before** uploading these files
* This code is **not** used for the final Lunabotics rover hardware

---

## 📌 Purpose

> **ESP32-S3 code was used for early testing and validation before transitioning to the ESP32-WROOM rover controller.**

