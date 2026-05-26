# Lunabotics Teleoperation – NVIDIA Jetson Orin NX

## Overview

This package provides the teleoperation framework used for the UHCL NASA Lunabotics rover platform running on an NVIDIA Jetson Orin NX. The system enables real-time rover control through ROS 2, allowing velocity commands to be generated from an Xbox controller and transmitted to embedded controllers for low-level actuation.

The architecture integrates high-level robotics software running on the Jetson with ESP32-based embedded controllers responsible for motor and actuator control.

---

## Features

- ROS 2-based teleoperation framework
- Xbox controller integration
- Real-time `/cmd_vel` command generation
- Differential-drive rover control
- Integration with ESP32 microcontrollers through micro-ROS
- Designed for physical rover deployment and validation
- Supports future autonomy integration using perception systems

---

## System Architecture

```text
Xbox Controller
       ↓
joy_node
       ↓
teleop_twist_joy
       ↓
geometry_msgs/Twist (/cmd_vel)
       ↓
Jetson Orin NX
       ↓
micro-ROS / UART Communication
       ↓
ESP32 Embedded Controller
       ↓
PWM Motor Control
       ↓
Rover Drive Motors
```

---

## Hardware

### Compute

- NVIDIA Jetson Orin NX
- ESP32 Microcontroller

### Sensors / Interfaces

- Xbox Controller (Bluetooth)
- LiDAR (future integration)
- 3D Depth Camera (future integration)

### Communication

- ROS 2 Humble
- micro-ROS
- UART serial communication

---

## Software Dependencies

Required packages:

```bash
sudo apt install ros-humble-joy
sudo apt install ros-humble-teleop-twist-joy
sudo apt install ros-humble-xbox-controller
```

---

## Build Instructions

Navigate to the workspace:

```bash
cd ~/lunabotics_ws
```

Build package:

```bash
colcon build
```

Source workspace:

```bash
source install/setup.bash
```

---

## Launch

Launch teleoperation:

```bash
ros2 launch lunabotics_teleop rover_joystick_teleop.launch.py
```

Verify command output:

```bash
ros2 topic echo /cmd_vel
```

---

## Purpose

This package serves as the teleoperation interface for the UHCL NASA Lunabotics rover, supporting testing, manual operation, embedded systems integration, and future autonomous navigation research.

---

## Author

Matthew Garcia  
Computer Engineering | Embedded Systems & Robotics  
University of Houston–Clear Lake
NASA Lunabotics – Robotics & Embedded Systems Engineer
