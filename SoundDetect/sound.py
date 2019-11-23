#Monitors GPIO pin 40 for input. A sound module is set up on physical pin 40.
#https://pinout.xyz/pinout/wiringpi#
import RPi.GPIO as GPIO
import time
import datetime
import os

import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)

GPIO.setmode(GPIO.BCM)
SOUND_PIN = 17
GPIO.setup(SOUND_PIN, GPIO.IN)

count = 0

def DETECTED(SOUND_PIN):
   global count
   nowtime = datetime.datetime.now()
   count += 1
   text = str(count) + ". Sound Detected at "+ str(nowtime)
   print ("Sound Detected! " + str(nowtime) + " " + str(count))
   client.publish("ricameonanitcherry",text)
   #os.system("/home/pi/scripts/playfile.py")

   return nowtime
print ("Sound Module Test (CTRL+C to exit)")
time.sleep(1)
print ("Ready")

try:
   GPIO.add_event_detect(SOUND_PIN, GPIO.RISING, callback=DETECTED)
   while 1:
      time.sleep(1)
except KeyboardInterrupt:
   print (" Quit")
   GPIO.cleanup()