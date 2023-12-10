"""
Laser Range Measure Device
Fetching initial settings from Waveshare LC29H(BS) 

Created on 10 Dec 2023

:author: Ville Lepistö
:copyright: 1m2lab © 2023
:license: The GNU General Public License v3.0 https://www.gnu.org/licenses/gpl-3.0.en.html

version 0.0.1 
- Initial, and quite shitty code version, but working at staring point.

"""

import sys
import serial
import math
import time
import datetime
import pynmea2

def send_command(port, command, target):
#    print('Executing ' + command + ' expecting ' + target)
    command = pynmea2.parse(command).render() + "\r\n"
#    print(command)
    port.flushInput()
    port.write(command.encode())
#    print('Executing command . . .')

    if target != 'no response message':
        log = []
        i, g = 0, 0
        while i < 500:
            i += 1
            line = port.readline().decode('utf-8', errors='ignore')
            log.append(line)
 #           print(line)
            if target in line:
 #               print('\nSuccess!\n' + line)
                return line.splitlines()[0]
                break 

        else:
            print('Response message not found.')

    else:
        print('Response message not expected for this command.')
        
# Setup serial

baud = 115200           # default
com_port = "/dev/ttyUSB0"   #default, change for your reference
ser = serial.Serial(com_port, baud, parity='N', bytesize=8, stopbits=1, timeout=None)
ser.flushInput()









