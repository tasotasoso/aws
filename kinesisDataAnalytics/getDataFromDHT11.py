#dht11 library is protected by MIT license.
#Check resource URL. 
#https://github.com/szazo/DHT11_Python

import RPi.GPIO as GPIO
import dht11
import time
import datetime
import subprocess

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=14)

while True:
    result = instance.read()
    if result.is_valid():
        payload = 'temperature:' + str(result.temperature) + ',humidity:' + str(result.humidity)
	print(payload)
        subprocess.call("./IoT_post.sh %s" % payload , shell=True)
    time.sleep(1)