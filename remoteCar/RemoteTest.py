#!/usr/bin/python
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

import time
import atexit


# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

################################# DC motor test!
#myMotor = mh.getMotor(3)

FL = mh.getMotor(3)
FR = mh.getMotor(4)
BL = mh.getMotor(1)
BR = mh.getMotor(2)

# set the speed to start, from 0 (off) to 255 (max speed)
#myMotor.setSpeed(150)
#myMotor.run(Raspi_MotorHAT.FORWARD);
FL.setSpeed(100)
FR.setSpeed(100)
BL.setSpeed(100)
BR.setSpeed(100)


# turn on motor
#myMotor.run(Raspi_MotorHAT.RELEASE);

FL.run(Raspi_MotorHAT.RELEASE)
FR.run(Raspi_MotorHAT.RELEASE)
BL.run(Raspi_MotorHAT.RELEASE)
BR.run(Raspi_MotorHAT.RELEASE)

try:
	while (True):

		command = input('Please input a command: ')
		print "HERE! "
		if command == 'w':
			print "Forward! "
			FL.run(Raspi_MotorHAT.FORWARD)
			FR.run(Raspi_MotorHAT.FORWARD)
			BL.run(Raspi_MotorHAT.FORWARD)
			BR.run(Raspi_MotorHAT.FORWARD)
			


		elif command == "s":
			print "Backward! "
			FL.run(Raspi_MotorHAT.BACKWARD)
			FR.run(Raspi_MotorHAT.BACKWARD)
			BL.run(Raspi_MotorHAT.BACKWARD)
			BR.run(Raspi_MotorHAT.BACKWARD)
			

		elif command == "x":
			print "Release"
			FL.run(Raspi_MotorHAT.RELEASE)
			FR.run(Raspi_MotorHAT.RELEASE)
			BL.run(Raspi_MotorHAT.RELEASE)
			BR.run(Raspi_MotorHAT.RELEASE)
			

except KeyboardInterrupt:
	print "************* STOP  **************"
	atexit.register(turnOffMotors)
	time.sleep(1.0)
	pass

