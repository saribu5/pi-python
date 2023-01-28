import jspy #scuffed ass stolen code
import RPi.GPIO as GPIO
import pigpio
import time

servoX = 18
servoY = 12
Xduty = 1500
Yduty = 1500

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(servoX, GPIO.OUT)
#GPIO.setup(servoY, GPIO.OUT)

Xpwm = pigpio.pi()
Ypwm = pigpio.pi()
Xpwm.set_mode(servoX, pigpio.OUTPUT)
Ypwm.set_mode(servoY, pigpio.OUTPUT)
Xpwm.set_PWM_frequency(servoX, 50)
Ypwm.set_PWM_frequency(servoY, 50)


try:
	while True:
		key, val = jspy.jsmain()
		print(key)
		print(val)

		if(key == "x"):
			if(val > 0):
				Xduty = Xduty + 25
			elif(val < 0):
				Xduty = Xduty - 25

			if(Xduty < 500):
				Xduty = 500
			elif(Xduty > 2000):
				Xduty = 2000
			else:
				Xpwm.set_servo_pulsewidth(servoX, Xduty)

		elif(key == "y"):
			if(val > 0):
				Yduty = Yduty + 25
			elif(val < 0):
				Yduty = Yduty - 25

			if(Yduty < 500):
				Yduty = 500
			elif(Yduty > 2000):
				Yduty = 2000
			else:
				Ypwm.set_servo_pulsewidth(servoY, Yduty)


except KeyboardInterrupt:
		GPIO.cleanup()

