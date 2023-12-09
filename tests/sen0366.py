"""
Laser Range Measure Device
initial testing Python3 script for RDRobot SEN0366 laser measuring sensor

Created on 09 Dec 2023

:author: Ville Lepistö
:copyright: 1m2lab © 2023
:license: The GNU General Public License v3.0 https://www.gnu.org/licenses/gpl-3.0.en.html

version 0.0.1 
- Initial, and quite shitty code version, but working at staring point.

"""


import serial
import time

# Define the serial port
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Change 'COM2' to your actual serial port

buff = bytearray([0x80, 0x06, 0x03, 0x77])                      #Set continious reading 
buffclose = bytearray([0x80, 0x04, 0x02, 0x7A])                 #Shut down device 
buffmeaspoint = bytearray([0xFA, 0x04, 0x08, 0x01, 0xF9])       #Set measuring point on top of device 
buffrange = bytearray([0xFA, 0x04, 0x09, 0x1E, 0xDB])           #Set mesauring range to 30 meters
bufffreq = bytearray([0xFA, 0x04, 0x0A, 0x00, 0xF8])            #Set frequency to 1s
buffresolution = bytearray([0xFA, 0x04, 0x0C, 0x01, 0xF5])      #Set resolution to 1mm
buffinterval = bytearray([0xFA, 0x04, 0x05, 0x01, 0xFC])        #Set time interval 1s 
calibration_value=-0.028                                        #Calibration value in meters. This must be done occacionally.

data = bytearray([0] * 11)

def calculate_checksum(data):
    checksum = sum(data[:10]) & 0xFF
    return (~checksum + 1) & 0xFF

def convert_to_distance(data):
    if data[3:6] == b'ERR':
        print("Out of range")
    else:

        hundreds = float(chr(data[3])) * 100
        tens = float(chr(data[4])) * 10
        ones = float(chr(data[5])) * 1
        oneones = float(chr(data[7])) * 0.1
        onetens = float(chr(data[8])) * 0.01
        onehundreds = float(chr(data[9])) * 0.001

        distance = hundreds + tens + ones + oneones + onetens + onehundreds
        distance = distance + calibration_value
        print(f"Distance = {distance:.3f} M")

ser.write(buffmeaspoint)
ser.write(buffrange)
ser.write(bufffreq)
ser.write(buffresolution)

try:
    # Main loop
    while True:
        # Send data
        ser.write(buff)

        # Wait for data to be available
        time.sleep(0.1)

        if ser.in_waiting > 0:
            # Read data
            ser.readinto(data)

            # Calculate and check checksum
            received_checksum = data[10]
            calculated_checksum = calculate_checksum(data)

            if received_checksum == calculated_checksum:
                convert_to_distance(data)
            else:
                print("Invalid Data!")

        time.sleep(0.2)

except KeyboardInterrupt:
    ser.write(buffclose)
    ser.close()
    print("Serial port closed.")



