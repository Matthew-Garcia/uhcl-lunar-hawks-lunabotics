# 📐 Electrical Schematics – UHCL Lunar Hawks Lunabotics

This folder contains the **electrical schematics** for the UHCL Lunar Hawks Lunabotics rover.
All schematics were created in **KiCad** and document the rover’s **power system, motor control, and compute interfaces**.

---

## 📄 Files

### ⚡ `Lunabotics_Lunar_Hawks_Electrical_Schematic_01.2.pdf`

* **Main rover electrical schematic**
* Includes:

  * ESP32-WROOM motor control connections
  * L298N motor drivers (drive motors, excavator, actuator)
  * Power distribution (24 V / 12 V / 3.3 V)
  * Encoders, servo, and safety components (fuses, E-stop)

---

### 🧠 `Lunabotics_Lunar_Hawks_Electrical_Schematic_01.1 (40-Pin Header Connection).pdf`

* **Jetson Nano / Orin 40-pin header interface schematic**
* Documents:

  * Jetson GPIO, I2C, SPI, UART connections
  * Sensor interfaces (IMU, LiDAR, IR sensors)
  * USB and peripheral expansion

---

## 🛠 Notes

* These schematics describe the **hardware layer only**
* GPIO assignments correspond to the firmware in `firmware/`
* ROS 2 nodes interact with this hardware **indirectly** through the ESP32 and Jetson
Just say **next** 👍

