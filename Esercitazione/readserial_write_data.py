#!/usr/bin/python

import serial
import re
import requests

endpoint = "http://127.0.0.1:8086/write?db=contapersone"

ser = serial.Serial('/dev/ttyACM0')  # open serial port
# "Humidity: {} %, Temp: {} Celsius"
rx = re.compile (r'STATO: (?P<stato>.*) - IR1: (?P<ir1>.*) - IR2: (?P<ir2>.*) - Nr.Persone: (?P<numPersone>.*)\r')

while (True):
    l = ser.readline ()
    match = rx.search (l)
    if match:
        stato = match.group('stato')
        ir1 = match.group('ir1')
        ir2 = match.group('ir2')
        numPersone = match.group('numPersone')
        #print ("STATO: " + stato + " IR1: " + ir1 + " IR2: " + ir2 + " Numero persone:" + numPersone)

        data = "stato,sensore=sensore1 stato="+stato+",ir1="+ir1+",ir2="+ir2+",persone="+numPersone
        requests.post(url = endpoint, data = data)

        with open('/home/pi/public_html/stato.txt', 'w') as f:
          f.write(stato)
        with open('/home/pi/public_html/ir1.txt', 'w') as f:
          f.write(ir1)
        with open('/home/pi/public_html/ir2.txt', 'w') as f:
          f.write(ir2)
        with open('/home/pi/public_html/numero_persone.txt', 'w') as f:
          f.write(numPersone) 


ser.close()             # close port
