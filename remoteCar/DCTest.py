#!/usr/bin/python
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f)
speed_FL = 60
Speed_FR = 60
Speed_BL = 60
Speed_BR = 60

################################# DC motor test!
#myMotor = mh.getMotor(3)

FL = mh.getMotor(4)
FR = mh.getMotor(3)
BL = mh.getMotor(2)
BR = mh.getMotor(1)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

def left():
        print "Turn Left!  "
        FL.setSpeed(speed_FL - 30)
        FR.setSpeed(Speed_FR + 30)
        BL.setSpeed(Speed_BL - 30)
        BR.setSpeed(Speed_BR + 30)

        FL.run(Raspi_MotorHAT.FORWARD)
        FR.run(Raspi_MotorHAT.FORWARD)
        BL.run(Raspi_MotorHAT.FORWARD)
        BR.run(Raspi_MotorHAT.FORWARD)


def right():
        print "Turn Right!  "
        FL.setSpeed(speed_FL + 30)
        FR.setSpeed(Speed_FR - 30)
        BL.setSpeed(Speed_BL + 30)
        BR.setSpeed(Speed_BR - 30)

        FL.run(Raspi_MotorHAT.FORWARD)
        FR.run(Raspi_MotorHAT.FORWARD)
        BL.run(Raspi_MotorHAT.FORWARD)
        BR.run(Raspi_MotorHAT.FORWARD)

def forward():
        print "Forward!  "
        FL.setSpeed(speed_FL)
        FR.setSpeed(Speed_FR)
        BL.setSpeed(Speed_BL)
        BR.setSpeed(Speed_BR)

        FL.run(Raspi_MotorHAT.FORWARD)
        FR.run(Raspi_MotorHAT.FORWARD)
        BL.run(Raspi_MotorHAT.FORWARD)
        BR.run(Raspi_MotorHAT.FORWARD)
    
def backward():
        print "Backward!  "
        FL.setSpeed(speed_FL)
        FR.setSpeed(Speed_FR)
        BL.setSpeed(Speed_BL)
        BR.setSpeed(Speed_BR)

        FL.run(Raspi_MotorHAT.BACKWARD)
        FR.run(Raspi_MotorHAT.BACKWARD)
        BL.run(Raspi_MotorHAT.BACKWARD)
        BR.run(Raspi_MotorHAT.BACKWARD)



# set the speed to start, from 0 (off) to 255 (max speed)
#myMotor.setSpeed(150)
#myMotor.run(Raspi_MotorHAT.FORWARD);

FL.setSpeed(speed_FL)
FR.setSpeed(Speed_FR)
BL.setSpeed(Speed_BL)
BR.setSpeed(Speed_BR)

# turn on motor
#myMotor.run(Raspi_MotorHAT.RELEASE);

FL.run(Raspi_MotorHAT.RELEASE)
FR.run(Raspi_MotorHAT.RELEASE)
BL.run(Raspi_MotorHAT.RELEASE)
BR.run(Raspi_MotorHAT.RELEASE)

try:
	while (True):
		print "Forward! "
		FL.run(Raspi_MotorHAT.FORWARD)
		FR.run(Raspi_MotorHAT.FORWARD)
		BL.run(Raspi_MotorHAT.FORWARD)
		BR.run(Raspi_MotorHAT.FORWARD)

		print "\tSpeed up..."
		for i in range(100):
			FL.setSpeed(i)
			FR.setSpeed(i)
			BL.setSpeed(i)
			BR.setSpeed(i)
			time.sleep(0.01)

		print "\tSlow down..."
		for i in reversed(range(100)):
			FL.setSpeed(i)
			FR.setSpeed(i)
			BL.setSpeed(i)
			BR.setSpeed(i)
			time.sleep(0.01)

		print "Backward! "
		FL.run(Raspi_MotorHAT.BACKWARD)
		FR.run(Raspi_MotorHAT.BACKWARD)
		BL.run(Raspi_MotorHAT.BACKWARD)
		BR.run(Raspi_MotorHAT.BACKWARD)

		print "\tSpeed up..."
		for i in range(100):
			FL.setSpeed(i)
			FR.setSpeed(i)
			BL.setSpeed(i)
			BR.setSpeed(i)
			time.sleep(0.01)

		print "\tSlow down..."
		for i in reversed(range(100)):
			FL.setSpeed(i)
			FR.setSpeed(i)
			BL.setSpeed(i)
			BR.setSpeed(i)
			time.sleep(0.01)

		print "Turn Left"
		right()
		time.sleep(3.0)

		print "Turn Right"
		left()
		time.sleep(3.0)

		print "Release"
		FL.run(Raspi_MotorHAT.RELEASE)
		FR.run(Raspi_MotorHAT.RELEASE)
		BL.run(Raspi_MotorHAT.RELEASE)
		BR.run(Raspi_MotorHAT.RELEASE)
		time.sleep(1.0)

except KeyboardInterrupt:
	print "************* STOP  **************"
	atexit.register(turnOffMotors)
	time.sleep(1.0)
	pass

