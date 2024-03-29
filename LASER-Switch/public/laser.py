#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)

LedPin = 11    # pin11

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def loop():
	while True:
		print ('...led on')
		GPIO.output(LedPin, GPIO.HIGH)  # led on
		time.sleep(0.5)
		

def destroy():
	print ('led off...')
	GPIO.output(LedPin, GPIO.LOW) # led off
	time.sleep(0.5)
	GPIO.output(LedPin, GPIO.LOW)     # led off
	GPIO.cleanup()                     # Release resource

while True:
	setup()
	client.subscribe('ricameo/temp')
	loop()
destroy()