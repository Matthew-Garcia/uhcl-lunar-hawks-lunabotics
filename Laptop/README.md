Here is the specialized README for your **Laptop** folder, incorporating the specific hardware constraints and the technical logic of your Micro-ROS implementation.

***

# 💻 Laptop Development Environment (`uros_ws`)

This workspace serves as the primary engineering station for firmware development and hardware flashing. Due to the **Jetson Orin NX** utilizing an **ARM-based architecture**, it cannot natively execute the ESP32 flashing tools required for this project. Therefore, all embedded deployment is handled via this dedicated workstation.

## 🛠️ Hardware & OS Specs
* **Host Machine:** HP Victus 15.6" Laptop.
* **Storage:** External SSD boot drive.
* **Operating System:** Ubuntu 22.04.5 LTS (Jammy Jellyfish).
* **Target Hardware:** ESP32-WROOM-32.

## 📁 Firmware: `twist_subscriber`
The core logic resides in the `firmware/twist_subscriber/` directory.

* **`app.c`**: The main application file written in C for **FreeRTOS**. It implements a single micro-ROS node named `esp32_twist_sub`.
* **`app-colcon.meta`**: The build configuration file that manages transport layers (Serial) and compilation parameters for the micro-ROS build system.

## ⚙️ Logic & Kinematics
The firmware subscribes to the `/cmd_vel` topic and implements **Differential Drive (Arcade Drive)** kinematics to translate velocity commands into physical hardware actuation.



### Wheel Equations
The target velocity ($V$) for each side of the rover is calculated using the following inverse kinematics:

$$V_{right} = v + w \cdot \frac{L}{2}$$
$$V_{left} = v - w \cdot \frac{L}{2}$$

* **$v$**: Linear velocity ($x$).
* **$w$**: Angular velocity ($z$).
* **$L$**: Track width ($0.465\text{m}$).

### PWM Mapping
Calculated velocities are mapped to an **8-bit PWM duty cycle (0–255)** for the motor drivers:
$$PWM = |V_{side}| \cdot 200.0$$

## 🚀 Build & Flash Procedure
Execution flow within the `uros_ws` on the HP Victus:

1.  **Configure:** ```bash
    ros2 run micro_ros_setup configure_firmware.sh twist_subscriber --transport serial
    ```
2.  **Build:**
    ```bash
    ros2 run micro_ros_setup build_firmware.sh
    ```
3.  **Flash:**
    ```bash
    ros2 run micro_ros_setup flash_firmware.sh
    ```

***

### Why this is documented this way:
* **Cross-Platform Necessity:** Explicitly stating the ARM vs. x86 flashing constraint demonstrates a high level of systems engineering awareness.
* **Technical Proof:** Including the specific Ubuntu version and kinematics math proves the project's reproducibility and your technical depth.
