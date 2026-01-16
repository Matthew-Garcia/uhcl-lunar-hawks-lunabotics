# 🤖 ROS 2 Workspace – UHCL Lunar Hawks Lunabotics

This directory contains the **ROS 2 workspace** used for high-level control, communication, and integration for the UHCL Lunar Hawks Lunabotics rover.

ROS 2 nodes in this workspace run on the **host computer** (laptop, Jetson, or NUC) and communicate with the rover’s embedded controllers over the network.

---

## 📁 Directory Structure

```
ros2_ws/
└── src/
```

---

## 📦 `src/`

Contains ROS 2 packages used for:

* Joystick and teleoperation input
* Command generation (linear `v` and rotational `w` velocities)
* Communication bridges (e.g., micro-ROS / WebSocket bridges)
* Integration with simulation (`gazebo`, `rviz`)

Each package follows standard ROS 2 workspace conventions.

---

## 🔗 Relationship to Other Components

* **Firmware (`firmware/`)** runs on ESP32 boards and executes motor-level control
* **ROS 2 (`ros2_ws/`)** handles high-level logic and user input
* **Simulation (`simulation/`)** is used for testing and visualization before hardware deployment

---

## 🛠 Usage Notes

* Build the workspace using:

  ```bash
  colcon build
  ```
* Source the workspace before running nodes:

  ```bash
  source install/setup.bash
  ```
* This workspace does **not** run on the ESP32

---

## 📌 Rule of Thumb

> **High-level logic → ROS 2 (`ros2_ws/`)
> Low-level control → ESP32 firmware**
