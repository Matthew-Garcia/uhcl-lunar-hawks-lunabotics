# UHCL Lunar Hawks – Lunabotics Rover Workspace

🚀 Official development workspace for the University of Houston–Clear Lake (UHCL) Lunar Hawks
NASA Lunabotics Competition rover.

## Project Focus
- ROS 2–based rover architecture
- Micro-ROS integration (ESP32 ↔ Jetson)
- Motor control, sensing, autonomy, and telemetry
- Competition-ready electrical and software systems

## System Architecture
- High-level control: Jetson Orin Nano
- Real-time motor & sensor nodes: ESP32 (Micro-ROS)
- Middleware: ROS 2
- Simulation: Gazebo + RViz

## Repository Structure
- `ros2_ws/` – ROS 2 packages
- `firmware/` – ESP32 firmware (Micro-ROS)
- `hardware/` – wiring, schematics, power distribution
- `simulation/` – Gazebo & RViz assets
- `docs/` – system documentation

## Safety
All power systems include fusing, emergency stops, and staged voltage regulation.

## Team
UHCL Lunar Hawks – Lunabotics  
Electrical & Software Systems  
Maintainer: Matthew Garcia
