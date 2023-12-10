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

#Printout PQTMSVINSTATUS 
QUERY = ['PQTMSVINSTATUS','$PQTMSVINSTATUS']
response = send_command(ser, QUERY[0], QUERY[1])
#print(response.split(',')) #split string to array
print("MsgVer: " + response.split(',')[1] + " " +
 "TOW: " + response.split(',')[2] + " " +
 "Valid: " + response.split(',')[3] + " " +
 "Res0: " + response.split(',')[4] + " " +
 "Res1: " + response.split(',')[5] + " " +
 "Obs: " + response.split(',')[6] + " " +
 "CfgDur: " + response.split(',')[7] + " " +
 "MeanX: " + response.split(',')[8] + " " + 
 "MeanY: " + response.split(',')[9] + " " +
 "MeanZ: " + response.split(',')[10] + " " +
 "MeanAcc: " + response.split(',')[11].split('*')[0])

