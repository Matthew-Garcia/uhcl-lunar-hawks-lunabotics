# 🔌 MicroPython Firmware Binaries

This folder contains **precompiled MicroPython firmware binaries** used to flash the ESP32 boards for the UHCL Lunar Hawks Lunabotics project.

These `.bin` files are flashed **before** uploading any `boot.py` or `main.py` runtime code.

---

## 📦 Files

### 🟦 `ESP32_GENERIC-20250911-v1.26.1.bin`

* MicroPython firmware for **ESP32 (WROOM / generic ESP32)**
* Used for the **Lunabotics rover controller**
* Flashed prior to uploading rover runtime files (`boot.py`, `main.py`, `test.py`)
![esp32_wroom](https://github.com/user-attachments/assets/a0298b6b-bdad-490d-961e-675aac871552)

---

### 🟩 `ESP32_GENERIC_S3-20250911-v1.26.1.bin`

* MicroPython firmware for **ESP32-S3**
* Used for **non-rover / earlier development and testing**
* Supports WebSocket-based control code
![esp32_s3](https://github.com/user-attachments/assets/22149a1e-4395-4e5a-8a90-0cf1c152aaa1)


---

## 🛠 Usage Notes

* Flash using tools such as:

  * `esptool.py`
  * Thonny
  * ESP-IDF flashing tools
* Only one firmware image should be flashed per board
* Runtime files are uploaded **after flashing** and live on the ESP32’s internal flash

---

## 📌 Reminder

> **`.bin` files flash MicroPython — `boot.py` and `main.py` run MicroPython.**

