#!/usr/bin/python

################################################################################################################
# PREREQUISITES
#	Tornado Web Server for Python
#
# TROUBLESHOOTING:
#	Don't use Ctrl+Z to stop the program, use Ctrl+c.
#	If you use Ctrl+Z, it will not close the socket and you won't be able to run the program the next time.
#	If you get the following error:
#		"socket.error: [Errno 98] Address already in use "
#	Run this on the terminal:
#		"sudo netstat -ap |grep :9093"
#	Note down the PID of the process running it
#	And kill that process using:
#		"kill pid"
#	If it does not work use:
#		"kill -9 pid"
#	If the error does not go away, try changin the port number '9093' both in the client and server code
import time,sys,json

# Import the ArmRobot.py file (must be in the same directory as this file!).
from Adafruit_PWM_Servo_Driver import PWM
import RPi.GPIO as GPIO  
import threading
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import tornado.escape

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

def t_stop();
	mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)

def t_up();

def t_down();

def t_left();

def t_right();


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
FL.setSpeed(150)
FR.setSpeed(150)
BL.setSpeed(150)
BR.setSpeed(150)

# turn on motor
#myMotor.run(Raspi_MotorHAT.RELEASE);
FL.run(Raspi_MotorHAT.RELEASE);
FR.run(Raspi_MotorHAT.RELEASE);
BL.run(Raspi_MotorHAT.RELEASE);
BR.run(Raspi_MotorHAT.RELEASE);


try:
	while True:
            print "Forward!  "
            FL.run(Raspi_MotorHAT.FORWARD)
            FR.run(Raspi_MotorHAT.FORWARD)
            BL.run(Raspi_MotorHAT.FORWARD)
            BR.run(Raspi_MotorHAT.FORWARD)
            
            print "\tSpeed up..."
            for i in range(255):
                FL.setSpeed(i)
                FR.setSpeed(i)
                BL.setSpeed(i)
                BR.setSpeed(i)
                time.sleep(0.01)
                
            print "\tSlow down..."
            for i in reversed(range(255)):
                FL.setSpeed(i)
                FR.setSpeed(i)
                BL.setSpeed(i)
                BR.setSpeed(i)
                time.sleep(0.01)


            print "Backward!  "
            FL.run(Raspi_MotorHAT.BACKWARD)
            FR.run(Raspi_MotorHAT.BACKWARD)
            BL.run(Raspi_MotorHAT.BACKWARD)
            BR.run(Raspi_MotorHAT.BACKWARD)

            print "\tSpeed up..."
            for i in range(255):
                FL.setSpeed(i)
                FR.setSpeed(i)
                BL.setSpeed(i)
                BR.setSpeed(i)
                time.sleep(0.01)

            print "\tSlow down..."
            for i in reversed(range(255)):
                FL.setSpeed(i)
                FR.setSpeed(i)
                BL.setSpeed(i)
                BR.setSpeed(i)
                time.sleep(0.01)


	    print "Release"
	    FL.run(Raspi_MotorHAT.RELEASE)
	    FR.run(Raspi_MotorHAT.RELEASE)
       	    BL.run(Raspi_MotorHAT.RELEASE)
      	    BR.run(Raspi_MotorHAT.RELEASE)
      	    time.sleep(2.0)


except KeyboardInterrupt:
	print "************* STOP  **************"
	FL.run(Raspi_MotorHAT.RELEASE)
	FR.run(Raspi_MotorHAT.RELEASE)
	BL.run(Raspi_MotorHAT.RELEASE)
	BR.run(Raspi_MotorHAT.RELEASE)
	time.sleep(1.0)
	pass

