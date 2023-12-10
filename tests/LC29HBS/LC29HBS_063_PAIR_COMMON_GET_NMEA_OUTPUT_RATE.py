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
QUERY = ['PAIR063,0','$PAIR001,063']
response = send_command(ser, QUERY[0], QUERY[1])
print(response.split(',')) #split string to array
#print("Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Message output rate setting: " + response.split(',')[2].split('*')[0])
 
QUERY = ['PAIR063,1','$PAIR001,063']
response = send_command(ser, QUERY[0], QUERY[1])
print(response.split(',')) #split string to array
#print("Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Message output rate setting: " + response.split(',')[2].split('*')[0])
 
QUERY = ['PAIR063,2','$PAIR001,063']
response = send_command(ser, QUERY[0], QUERY[1])
print(response.split(',')) #split string to array
#print("Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Message output rate setting: " + response.split(',')[2].split('*')[0])
 
QUERY = ['PAIR063,3','$PAIR001,063']
response = send_command(ser, QUERY[0], QUERY[1])
print(response.split(',')) #split string to array
#print("Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Message output rate setting: " + response.split(',')[2].split('*')[0])
 
QUERY = ['PAIR063,4','$PAIR001,063']
response = send_command(ser, QUERY[0], QUERY[1])
print(response.split(',')) #split string to array
#print("Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Message output rate setting: " + response.split(',')[2].split('*')[0])
 
QUERY = ['PAIR063,5','$PAIR001,063']
response = send_command(ser, QUERY[0], QUERY[1])
print(response.split(',')) #split string to array
#print("Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Message output rate setting: " + response.split(',')[2].split('*')[0])
 
QUERY = ['PAIR063,6','$PAIR001,063']
response = send_command(ser, QUERY[0], QUERY[1])
print(response.split(',')) #split string to array
#print("Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Message output rate setting: " + response.split(',')[2].split('*')[0])
 
QUERY = ['PAIR063,7','$PAIR001,063']
response = send_command(ser, QUERY[0], QUERY[1])
print(response.split(',')) #split string to array
#print("Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Message output rate setting: " + response.split(',')[2].split('*')[0])
 
QUERY = ['PAIR063,8','$PAIR001,063']
response = send_command(ser, QUERY[0], QUERY[1])
print(response.split(',')) #split string to array
#print("Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Message output rate setting: " + response.split(',')[2].split('*')[0])
 


