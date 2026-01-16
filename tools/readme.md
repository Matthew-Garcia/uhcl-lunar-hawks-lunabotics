# 🧰 Tools – Development & Teleoperation Utilities

This directory contains **helper tools and utility scripts** used during development, testing, and teleoperation of the UHCL Lunar Hawks Lunabotics rover.

The contents of this folder are **not part of the core firmware or ROS 2 runtime**, but support controller input, debugging, and system setup.

---

## 📁 Directory Structure

```
tools/
├── controller_nodes/
├── controller_python/
├── docs/
└── readme.md
```

---

## 🎮 `controller_nodes/`

Contains **Node.js–based controller and joystick bridge tools**, including:

* Xbox / PS5 controller input handling
* Joystick debugging and value inspection
* WebSocket-based command forwarding to the rover

These scripts are typically used for **manual teleoperation and testing**.

---

## 🐍 `controller_python/`

Contains **Python-based controller utilities**, including:

* `controller.py` – reads gamepad input (via `evdev`)
* Applies deadzones and calibration
* Sends **linear (`v`) and rotational (`w`) velocity commands** over WebSockets

This is an alternative controller implementation to the Node.js tools.

---

## 📚 `docs/`

Contains **supporting documentation** related to tool usage, setup, or drivers (e.g., controller drivers or system configuration notes).

---

## 🛠 Usage Notes

* These tools run on a **host computer or Jetson**, not on the ESP32
* They are intended for:

  * Development
  * Debugging
  * Manual rover control
* Only **one controller tool** should be active at a time

---

## 📌 Rule of Thumb

> **If it helps you develop, test, or control the rover—but isn’t firmware or ROS—it lives in `tools/`.**

