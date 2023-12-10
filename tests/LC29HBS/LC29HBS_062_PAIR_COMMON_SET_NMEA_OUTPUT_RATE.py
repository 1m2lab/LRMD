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
QUERY = ['PAIR062,0,1','$PAIR001,062']
response = send_command(ser, QUERY[0], QUERY[1])
print(response.split(',')) #split string to array
#print("Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Message output rate setting: " + response.split(',')[2].split('*')[0])
 
QUERY = ['PAIR062,1,1','$PAIR001,062']
response = send_command(ser, QUERY[0], QUERY[1])
print(response.split(',')) #split string to array
#print("Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Message output rate setting: " + response.split(',')[2].split('*')[0])
 
QUERY = ['PAIR062,2,1','$PAIR001,062']
response = send_command(ser, QUERY[0], QUERY[1])
print(response.split(',')) #split string to array
#print("Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Message output rate setting: " + response.split(',')[2].split('*')[0])
 
QUERY = ['PAIR062,3,1','$PAIR001,062']
response = send_command(ser, QUERY[0], QUERY[1])
print(response.split(',')) #split string to array
#print("Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Message output rate setting: " + response.split(',')[2].split('*')[0])
 
QUERY = ['PAIR062,4,1','$PAIR001,062']
response = send_command(ser, QUERY[0], QUERY[1])
print(response.split(',')) #split string to array
#print("Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Message output rate setting: " + response.split(',')[2].split('*')[0])
 
QUERY = ['PAIR062,5,1','$PAIR001,062']
response = send_command(ser, QUERY[0], QUERY[1])
print(response.split(',')) #split string to array
#print("Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Message output rate setting: " + response.split(',')[2].split('*')[0])
 
QUERY = ['PAIR062,6,1','$PAIR001,062']
response = send_command(ser, QUERY[0], QUERY[1])
print(response.split(',')) #split string to array
#print("Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Message output rate setting: " + response.split(',')[2].split('*')[0])
 
QUERY = ['PAIR062,7,1','$PAIR001,062']
response = send_command(ser, QUERY[0], QUERY[1])
print(response.split(',')) #split string to array
#print("Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Message output rate setting: " + response.split(',')[2].split('*')[0])
 
QUERY = ['PAIR062,8,1','$PAIR001,062']
response = send_command(ser, QUERY[0], QUERY[1])
print(response.split(',')) #split string to array
#print("Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Type of standard NMEA sentence: " + response.split(',')[1] + " " +
 #"Message output rate setting: " + response.split(',')[2].split('*')[0])
 


