#!/usr/bin/python

import serial
import re

ser = serial.Serial('/dev/ttyACM0')  # open serial port
# "Humidity: {} %, Temp: {} Celsius"
rx = re.compile (r'STATO: (?P<stato>.*) - IR1: (?P<ir1>.*) - IR2: (?P<ir2>.*) Nr.Persone: (?P<numPersone>.*)')

while (True):
    l = ser.readline ()
    match = rx.search (l)
    if match:
        stato = match.group('stato')
        ir1 = match.group('ir1')
        ir2 = match.group('ir2')
        numPersone = match.group('numPersone')
        print ("STATO: " + stato + " IR1: " + ir1 + " IR2: " + ir2 + " Numero persone:" + numPersone)

ser.close()             # close port