<p align="center">
  <img src="https://github.com/user-attachments/assets/68e6a4ce-1887-474b-bf27-83c9a26805da" width="300" alt="UHCL Lunar Hawks Logo">
</p>

<h1 align="center">🚀 UHCL Lunar Hawks – NASA Lunabotics Stack</h1>

<p align="center">
  <strong>The official development workspace for the University of Houston–Clear Lake (UHCL) robotic lunar excavator.</strong>
</p>

<p align="center">
  <a href="https://matthew-garcia-portfolio.vercel.app/">
    <img src="https://img.shields.io/badge/Portfolio-Vercel-black?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio">
  </a>
  <a href="https://www.linkedin.com/in/matthew-garcia-ce/">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/ROS2-Humble-blue?style=flat-square&logo=ros" alt="ROS 2">
  <img src="https://img.shields.io/badge/Hardware-Jetson%20Orin%20Nano-green?style=flat-square&logo=nvidia" alt="Jetson">
  <img src="https://img.shields.io/badge/Firmware-ESP32%20(Micro--ROS)-red?style=flat-square&logo=espressif" alt="ESP32">
</p>

---

## 🛰️ About the Project
This repository houses the software and electrical architecture for the **Lunar Hawks** rover, built for the [NASA Lunabotics Competition](https://www.nasa.gov/learning-resources/lunabotics-challenge/). 

The challenge requires collegiate teams to apply the **NASA Systems Engineering** process to design and build a prototype robot capable of navigating a simulated lunar environment, excavating regolith, and constructing berm structures to support future Artemis missions.

## 🛠️ System Architecture
As the **Systems Integration Lead**, my focus was on creating a robust interface between high-level autonomy and low-level electromechanical control.

* **Compute:** NVIDIA Jetson Orin Nano for LiDAR processing, SLAM, and autonomy.
* **Embedded:** ESP32 nodes running **Micro-ROS** to handle real-time motor control and sensor feedback.
* **Navigation:** LiDAR-based obstacle detection and cost-map generation.
* **Power:** Modular power distribution system with integrated E-Stop safety protocols and voltage regulation.

## 📂 Repository Structure
| Directory | Description |
| :--- | :--- |
| `ros2_ws/` | Main ROS 2 workspace, navigation nodes, and custom message definitions. |
| `firmware/` | Micro-ROS firmware for ESP32 motor drivers and sensor suites. |
| `hardware/` | Pinout diagrams, electrical schematics, and PDU maps. |
| `simulation/` | URDF models and Gazebo environments for digital twin validation. |
| `docs/` | Systems Engineering Paper and technical documentation. |

## 👷 Lead Maintainer
**Matthew Garcia** *Computer Engineering Graduate (B.S. May 2026)* University of Houston–Clear Lake  
[Portfolio](https://matthew-garcia-portfolio.vercel.app/) | [LinkedIn](https://www.linkedin.com/in/matthew-garcia-ce/)

---
<p align="center">Built with 💙 by the UHCL Lunar Hawks Electrical & Software Team</p>
