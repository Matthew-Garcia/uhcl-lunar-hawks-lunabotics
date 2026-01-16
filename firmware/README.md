# 🔧 Firmware – UHCL Lunar Hawks Lunabotics

This directory contains all **ESP32-related firmware** used in the UHCL Lunar Hawks Lunabotics project.
It includes both **MicroPython firmware binaries** (used to flash boards) and **runtime files** that execute directly on the ESP32 hardware.

---

## 📁 Directory Structure

```
firmware/
├── micropython_bins/
│   ├── ESP32_GENERIC-20250911-v1.26.1.bin
│   ├── ESP32_GENERIC_S3-20250911-v1.26.1.bin
│   └── readme.md
│
├── esp32_wroom/
│   └── flash/
│       ├── boot.py
│       ├── main.py
│       └── test.py
│
└── esp32_s3/
    └── flash/
        ├── boot.py
        └── main.py
```

---

## 🔌 `micropython_bins/`

Contains **precompiled MicroPython `.bin` files** used to flash ESP32 boards.

* These files are flashed **once** (or when updating MicroPython)
* Flashing is done using tools such as:

  * `esptool.py`
  * Thonny
  * ESP-IDF tools

After flashing, runtime files are uploaded separately.

---

## 🤖 `esp32_wroom/flash/`

Runtime files for the **ESP32-WROOM rover controller**.

![esp32_wroom](https://github.com/user-attachments/assets/f7b276a8-e1b6-4f32-987b-851161840848)

Includes:

* `boot.py` – safe startup and Wi-Fi connection
* `main.py` – rover control logic (linear & rotational velocity, motor control, tank turns, actuators, WebSocket server)
* `test.py` – standalone wheel and motor test utility

These files live on the ESP32’s internal flash and execute under MicroPython.

---

## 🧪 `esp32_s3/flash/`

Runtime files for the **ESP32-S3**, used for **non-rover / earlier development and testing**.

![esp32_s3](https://github.com/user-attachments/assets/2a5e210d-57bb-4e45-ac03-9d9507b15d2d)

Includes:

* `boot.py` – Wi-Fi setup
* `main.py` – WebSocket-based linear (`v`) and rotational (`w`) velocity control for a simpler differential-drive setup

---

## ⚠️ Important Notes

* ESP32 firmware files **do NOT belong in `ros2_ws/src`**
* ROS 2 nodes (e.g. `controller.py`) run on the **computer**, not on the ESP32
* Only one `main.py` runs automatically on an ESP32 at a time

---

## 📌 Rule of Thumb

> **If it runs on the ESP32 → it belongs in `firmware/`.
> If it runs in ROS → it belongs in `ros2_ws/src`.**
