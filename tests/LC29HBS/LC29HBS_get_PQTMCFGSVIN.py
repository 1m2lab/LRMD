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
QUERY = ['PQTMCFGSVIN,R','$PQTMCFGSVIN']
response = send_command(ser, QUERY[0], QUERY[1])
#print(response.split(',')) #split string to array
print("Mode: " + response.split(',')[2] + " MinDur: " + 
 response.split(',')[3] + " " +  " 3D_AccLimit: " + 
 response.split(',')[4] + " " +  " ECEF_X: " + 
 response.split(',')[5] + " " +  " ECEF_Y: " + 
 response.split(',')[6] + " " +  " ECEF_Z: " +  
 response.split(',')[7].split('*')[0])







