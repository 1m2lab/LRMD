# LRMD
Laser Range Measuring Device aka. LRMD is a device under development for Drone based surveying. The device will measure distance between Drone and ground surface and decrease the value from RTK geoid height which accomplish relative accurate measurement e.g. drainage and surface water management design with 3D modeling programs.

# Python implementation of DFRobot SKU0366
The project will FDRobot Infrared Laser Distance Sensor (50m/80m) https://wiki.dfrobot.com/Infrared_Laser_Distance_Sensor_50m_80m_SKU_SEN0366
This will give relatively accurate tool for this project. Sensor has arduino implementation: https://wiki.dfrobot.com/Infrared_Laser_Distance_Sensor_50m_80m_SKU_SEN0366

# LRMD unit
Unit are based on Raspberry Pi Zero 2w and Waveshare LC29H(BS) RTK Hat, with GY-9250 / GY-6500 sensor (for Z-axis corrections and Magnetic Heading for device) and ZeroCam NOIR Camera. Device are going to be designed for 2 purposes: land-based surveying and drone-based surveying. These all will be run on Dietpi v8.24 64bit (bookworm) Linux-distro. There is more tu come later :)

EDIT 20231210: Distro swapped to RaspiOS bullseye 64bit due inop of camera in Dietpi.
 
