# 🛠 Hardware – UHCL Lunar Hawks Lunabotics

This directory contains **hardware documentation** for the UHCL Lunar Hawks Lunabotics rover, including electrical schematics and system-level hardware design information.

The contents of this folder describe the **physical and electrical architecture** of the rover and support the firmware and software components in the repository.

---

## 📁 Directory Structure

```
hardware/
└── schematics/
```

---

## 📐 `schematics/`

Contains **electrical schematics** created in **KiCad**, documenting:

* Power distribution (24 V, 12 V, 3.3 V)
* Motor drivers and actuators
* ESP32-WROOM control connections
* Jetson Nano / Orin 40-pin header interfaces
* Sensors, encoders, and safety components (fuses, E-stop)

See `hardware/schematics/README.md` for detailed descriptions of each schematic file.

---

## 🔗 Relationship to Other Folders

* **Firmware (`firmware/`)** implements control logic that corresponds to GPIO and interfaces defined here
* **ROS 2 (`ros2_ws/`)** runs on the host computer and interacts with hardware indirectly
* **Hardware schematics** serve as the reference for wiring, debugging, and validation

---

## 📌 Rule of Thumb

> **If it’s physical or electrical → it belongs in `hardware/`.**
You’re building this repo exactly the way real robotics teams do — this is solid work 💪🚀

