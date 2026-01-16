# 🧠 Jetson – High-Level Compute

This directory contains files related to the **NVIDIA Jetson** platform used as the **high-level compute unit** for the UHCL Lunar Hawks Lunabotics rover.

The Jetson is responsible for running **ROS 2**, managing system-level logic, and bridging communication between onboard sensors and the rover’s embedded controllers.

---

## 📁 Directory Structure

```
jetson/
├── launch/
├── setup/
└── README.md
```

---

## 🚀 `launch/`

Contains **ROS 2 launch files** used to start:

* Control nodes
* Communication bridges (e.g., micro-ROS / WebSocket)
* Sensor pipelines
* Visualization tools (when applicable)

---

## ⚙️ `setup/`

Contains **setup and configuration documentation** for the Jetson platform, including:

* micro-ROS installation notes
* System dependencies
* Network and interface configuration
* Environment setup for ROS 2

---

## 🔗 Relationship to Other Components

* **Jetson (`jetson/`)** runs high-level computation and ROS 2 nodes
* **Firmware (`firmware/`)** runs on ESP32 boards for low-level control
* **Simulation (`simulation/`)** is used for validation and testing
* **Hardware (`hardware/`)** defines physical interfaces and wiring

---

## 🛠 Notes

* This directory may expand to include:

  * Sensor drivers
  * Perception and autonomy nodes
  * System monitoring tools
* Not all features may be active at the same time

---

## 📌 Purpose

> **High-level logic and coordination live on the Jetson.**
