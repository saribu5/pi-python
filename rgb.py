#essentially just aaron dicking around with the gpio pins on a raspberry pi
#nothing more than that
import RPi.GPIO as GPIO	
import time
import random
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT) #red out
GPIO.setup(32, GPIO.OUT) #green out
GPIO.setup(33, GPIO.OUT) #blue out
#pwm start
r = GPIO.PWM(12, 400)
g = GPIO.PWM(32, 400)
b = GPIO.PWM(33, 400)

#color values
red = 0
green = 0
blue = 0

#start pwm
r.start(0)
g.start(0)
b.start(0)

while True:
	#changing the led color
	for i in range(255):
		red += 1
		print(red, green, blue)
		time.sleep(0.01)
		r.ChangeDutyCycle((i/255)*100)
	for i in range(255):
		blue += 1
		print(red, green, blue)
		time.sleep(0.01)
		b.ChangeDutyCycle((i/255)*100)
	for i in range(255):
		red -= 1
		print(red, green, blue)
		time.sleep(0.01)
		r.ChangeDutyCycle((i/255)*100)
	for i in range(255):
		green += 1
		print(red, green, blue)
		time.sleep(0.01)
		g.ChangeDutyCycle((i/255)*100)
	for i in range(255):
		blue -= 1
		print(red, green, blue)
		time.sleep(0.01)
		b.ChangeDutyCycle((i/255)*100)
	for i in range(255):
		red += 1
		print(red, green, blue)
		time.sleep(0.01)
		r.ChangeDutyCycle((i/255)*100)
	for i in range(255):
		green -= 1
		print(red, green, blue)
		time.sleep(0.01)
		g.ChangeDutyCycle((i/255)*100)
	for i in range(255):
		red -= 1
		print(red, green, blue)
		time.sleep(0.01)
		r.ChangeDutyCycle((i/255)*100)
GPIO.cleanup()
