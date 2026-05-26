# CAD Models – NASA Lunabotics Rover

## Overview

This directory contains CAD models, assemblies, and mechanical design files used in the development of the UHCL NASA Lunabotics rover platform. These models support subsystem integration, component placement, prototyping, and validation of mechanical structures for lunar excavation operations.

The CAD workflow is used to evaluate fitment, mounting configurations, manufacturability, and system-level integration between electrical, mechanical, and embedded subsystems.

---

## Objectives

- Develop rover mechanical structures and assemblies
- Validate subsystem fitment and packaging
- Support sensor and actuator placement
- Improve maintainability and serviceability
- Enable rapid prototyping and design iteration
- Support manufacturing and future design revisions

---

## Design Areas

### Structural Components

- Chassis structures
- Mounting brackets
- Sensor mounts
- Electronics enclosures
- Wheel assemblies
- Actuator interfaces

### Electrical / Embedded Integration

- Jetson mounting configurations
- ESP32 controller placement
- Battery and power system packaging
- Wiring routing and cable management
- Connector accessibility

### Robotics Integration

- LiDAR mounting
- Camera mounting
- 3D depth sensor placement
- Mechanical support for autonomous systems

---

## CAD Tools Used

- Fusion 360
- SolidWorks
- Onshape
- STEP/STL conversion tools

---

## File Types

| Extension | Purpose |
|-----------|----------|
| .f3d | Fusion 360 project files |
| .step / .stp | Universal CAD exchange files |
| .stl | 3D printing and mesh files |
| .sldprt | SolidWorks part files |
| .sldasm | SolidWorks assembly files |

---

## Design Workflow

```text
Concept Requirements
        ↓
CAD Modeling
        ↓
Assembly Integration
        ↓
Subsystem Packaging
        ↓
Mechanical Validation
        ↓
Prototype Iteration
        ↓
Manufacturing / Deployment
```

---

## Design Considerations

During development, emphasis is placed on:

- Mechanical robustness
- Weight reduction
- Serviceability
- Component accessibility
- Manufacturing feasibility
- Electrical and embedded system integration
- Real-world operational reliability

---

## Notes

Many CAD designs undergo multiple iterations during development and may include both custom-designed components and modified open-source/reference designs integrated into the rover platform.

---

## Author

Matthew Garcia  
Computer Engineer | Embedded Systems & Robotics  
University of Houston–Clear Lake  
NASA Lunabotics – Robotics & Embedded Systems Engineer
