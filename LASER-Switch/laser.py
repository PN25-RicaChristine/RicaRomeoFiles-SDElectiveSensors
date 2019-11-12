#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

LedPin = 11    # pin11

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def on_connect(client, userdata, flags, rc):
    client.subscribe("ricameo/temp")

def on_message(client, userdata, msg):
    print(msg.topic+" : "+str(msg.payload.decode("utf-8")))
    if str(msg.payload.decode("utf-8"))=="on":
    	setup()
    	print ('...led on')
    	GPIO.output(LedPin, GPIO.HIGH)  # led on
    elif str(msg.payload.decode("utf-8"))=="off":
    	print ('led off...')
    	GPIO.output(LedPin, GPIO.LOW) # led off
    	GPIO.cleanup() 

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()