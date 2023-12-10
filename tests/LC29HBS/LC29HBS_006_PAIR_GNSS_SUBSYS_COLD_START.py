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
from serial_send_command import *


#getting initial settings, command target in array

#Printout
QUERY = ['PAIR006','$PAIR001']
response = send_command(ser, QUERY[0], QUERY[1])
print(response.split(',')) #split string to array
#print("Enable: " + response.split(',')[1].split('*')[0])







