#Monitors GPIO pin 40 for input. A sound module is set up on physical pin 40.
#https://pinout.xyz/pinout/wiringpi#
import RPi.GPIO as GPIO
import time
import datetime


import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)

GPIO.setmode(GPIO.BCM)
SOUND_PIN = 17
GPIO.setup(SOUND_PIN, GPIO.IN)

count = 0

passedTime = []

def DETECTED(SOUND_PIN):
   global count
   # nowtime = datetime.datetime.utcnow()
   count += 1
   # text = str(count) + ". Sound Detected at "+ str(nowtime)
   # text ="Sound Detected at "+ str(nowtime)
   # print ("Sound Detected! " + str(nowtime) + " " + str(count))
   print("Sound Detected!")
   client.publish("ricameonanitcherry","Reach Noisy Level!" )


def NODETECTED(SOUND_PIN):
	print("No Detected")
print ("Sound Module Test (CTRL+C to exit)")
time.sleep(1)
print ("Ready")


# GPIO.add_event_detect(SOUND_PIN, GPIO.RISING, callback=DETECTED)

# while True:
# 	# GPIO.add_event_detect(SOUND_PIN, GPIO.FALLING, callback=NODETECTED)
# 	print("while True:")


try:
   GPIO.add_event_detect(SOUND_PIN, GPIO.RISING, bouncetime=1000)
   GPIO.add_event_callback(SOUND_PIN, callback=DETECTED)
   while 1:
      time.sleep(0.5)
      client.publish("ricameonanitcherry","Not Noisy")
      print("None")
      # print("SOUND_PIN: " + str(GPIO.input(SOUND_PIN)))
except KeyboardInterrupt:
   print (" Quit")
   GPIO.cleanup()