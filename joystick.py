import jspy #scuffed ass stolen code
import RPi.GPIO as GPIO
import pigpio
import time

#quick tutorial time on how to use
#so plug stuff in and whatever right
#run command "sudo pigpiod" for the gpio  pins cause you need those


servoX = 18
servoY = 12
Xduty = 1500
Yduty = 1500

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

		if(key == "x" or key == "hat0x"):
			if(val > 0):
				Xduty = Xduty + 25
			elif(val < 0):
				Xduty = Xduty - 25

			if(Xduty < 500):
				Xduty = 500
			elif(Xduty > 2500):
				Xduty = 2500
			else:
				Xpwm.set_servo_pulsewidth(servoX, Xduty)

		elif(key == "y" or key == "hat0y"):
			if(val > 0):
				Yduty = Yduty + 25
			elif(val < 0):
				Yduty = Yduty - 25

			if(Yduty < 500):
				Yduty = 500
			elif(Yduty > 2500):
				Yduty = 2500
			else:
				Ypwm.set_servo_pulsewidth(servoY, Yduty)
		elif(key == "cross"):
			Xduty = 1500
			Yduty = 1500
			Xpwm.set_servo_pulsewidth(servoX, Xduty)
			Ypwm.set_servo_pulsewidth(servoY, Yduty)


except KeyboardInterrupt:
	print("interrupt")
