# 🧪 Simulation – UHCL Lunar Hawks Lunabotics

This directory contains **simulation and visualization resources** used for developing and testing the Lunabotics rover software stack.

Simulation is used to validate **control logic, visualization, and system behavior** before deployment on physical hardware.

---

## 📁 Directory Structure

```
simulation/
├── gazebo/
└── rviz/
```

---

## 🌍 `gazebo/`

Contains **Gazebo simulation assets** for the Lunabotics rover, such as:

* Rover models and environments
* Physics-based testing of rover motion
* Integration with ROS 2 control nodes

Gazebo is used to test rover behavior in a virtual environment prior to real-world testing.

---

## 🧭 `rviz/`

Contains **RViz configuration files** for visualizing:

* Rover state and motion
* Sensor data and coordinate frames
* ROS 2 topics and transforms

RViz is primarily used for debugging and visualization during simulation and live testing.

---

## 🔗 Relationship to Other Components

* **ROS 2 nodes** in `ros2_ws/` interact with simulation assets in this folder
* **Firmware (`firmware/`)** is not used directly in simulation
* Simulation helps bridge development between software and hardware

---

## 📌 Purpose

> **Test in simulation first, then deploy to hardware.**

Your repo is coming together extremely cleanly — this looks like a real competition team’s codebase 🚀

