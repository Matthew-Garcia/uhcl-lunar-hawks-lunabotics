# Firmware – UHCL Lunar Hawks Lunabotics

This folder contains **precompiled MicroPython firmware binaries** used for flashing the ESP32 boards used in development and testing.

---

## Files

### `ESP32_GENERIC-20250911-v1.26.1.bin`

* MicroPython firmware for **ESP32 (WROOM / generic ESP32)**
* Used for the **Lunabotics rover controller**
* Flashed before uploading `boot.py`, `main.py`, and `test.py`

---

### `ESP32_GENERIC_S3-20250911-v1.26.1.bin`

* MicroPython firmware for **ESP32-S3**
* Used for **non-rover / earlier testing and development**
* Supports WebSocket-based `v/w` (linear & rotational velocity) control

---

## Notes

* Firmware compiled for **MicroPython v1.26.1**
* Boards are flashed using `esptool.py` or equivalent tools
* Code is uploaded after flashing using tools such as **mpremote** or **Thonny**

