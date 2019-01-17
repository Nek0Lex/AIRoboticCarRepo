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

import atexit
import carSpeed

# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f)

FL = mh.getMotor(4)
FR = mh.getMotor(3)
BL = mh.getMotor(2)
BR = mh.getMotor(1)

FL.setSpeed(carSpeed.speed_FL)
FR.setSpeed(carSpeed.speed_FR)
BL.setSpeed(carSpeed.speed_BL)
BR.setSpeed(carSpeed.speed_BR)

# Variables
c=0
angle = carSpeed.turningAngle
acceleration = 0
angleChanged = 0

def turnOffMotors():
	mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)

# recommended for auto-disabling motors on shutdown!
atexit.register(turnOffMotors())

def setAngle(angle):
  global angleChanged
  angleChanged = angle

def setSpeed(acc):
  global acceleration
  acceleration= acc

def forward():
        print "acceleration in forward"
        print acceleration
        FL.setSpeed(carSpeed.speed_FL+acceleration)
        FR.setSpeed(carSpeed.speed_FR+acceleration)
        BL.setSpeed(carSpeed.speed_BL+acceleration)
        BR.setSpeed(carSpeed.speed_BR+acceleration)

        FL.run(Raspi_MotorHAT.FORWARD)
        FR.run(Raspi_MotorHAT.FORWARD)
        BL.run(Raspi_MotorHAT.FORWARD)
        BR.run(Raspi_MotorHAT.FORWARD)
    
def backward():
        FL.setSpeed(carSpeed.speed_FL)
        FR.setSpeed(carSpeed.speed_FR)
        BL.setSpeed(carSpeed.speed_BL)
        BR.setSpeed(carSpeed.speed_BR)

        FL.run(Raspi_MotorHAT.BACKWARD)
        FR.run(Raspi_MotorHAT.BACKWARD)
        BL.run(Raspi_MotorHAT.BACKWARD)
        BR.run(Raspi_MotorHAT.BACKWARD)

def left():
        FL.setSpeed(carSpeed.speed_FL - angle - angleChanged)
        FR.setSpeed(carSpeed.speed_FR + angle + angleChanged)
        BL.setSpeed(carSpeed.speed_BL - angle - angleChanged)
        BR.setSpeed(carSpeed.speed_BR + angle + angleChanged)

        # FL.run(Raspi_MotorHAT.FORWARD)
        # FR.run(Raspi_MotorHAT.FORWARD)
        # BL.run(Raspi_MotorHAT.FORWARD)
        # BR.run(Raspi_MotorHAT.FORWARD)


def right():
        FL.setSpeed(carSpeed.speed_FL + angle + angleChanged)
        FR.setSpeed(carSpeed.speed_FR - angle - angleChanged)
        BL.setSpeed(carSpeed.speed_BL + angle + angleChanged)
        BR.setSpeed(carSpeed.speed_BR - angle - angleChanged)

        # FL.run(Raspi_MotorHAT.FORWARD)
        # FR.run(Raspi_MotorHAT.FORWARD)
        # BL.run(Raspi_MotorHAT.FORWARD)
        # BR.run(Raspi_MotorHAT.FORWARD)

try:
    
        #Initialize TOrnado to use 'GET' and load index.html
        class MainHandler(tornado.web.RequestHandler):
          def get(self):
            loader = tornado.template.Loader(".")
            self.write(loader.load("index.html").generate())

        #Code for handling the data sent from the webpage
        class WSHandler(tornado.websocket.WebSocketHandler):
                def open(self):
                        print 'connection opened...'
                def on_message(self, message):      # receives the data from the webpage and is stored in the variable message
                        global c
                        print 'received:', message        # prints the revived from the webpage 
                        decodejson = json.loads(message)
                        c=decodejson['eventType']
                        v=decodejson['eventValue']
                        print 'eventType:',c
                        if c == 8 :
                          print "Running Forward"
                          forward()

                        elif c == 2 :
                          print "Running Reverse"
                          backward()

                        elif c == 4 :
                          print "Turning Right"
                          right()

                        elif c == 6 :
                          print "Turning Left"
                          left()
                        elif c == 5 :
                          print "Stopped"
                          turnOffMotors()    # Stop the robot from moving.   	
                        elif c == 1 :
                          print "Angle Changed"
                          setAngle(v)

                        elif c == 3 :	  
                          print "Accelerate"
                          setSpeed(v)
                          		  		  		
                        print "Values Updated"

                def on_close(self):
                        # Stop the robot from moving.
                        print 'connection closed...'
                        turnOffMotors()

        application = tornado.web.Application([
          (r'/ws', WSHandler),
          (r'/', MainHandler),
          (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./resources"}),
        ])

        class myThread (threading.Thread):
            def __init__(self, threadID, name, counter):
                threading.Thread.__init__(self)
                self.threadID = threadID
                self.name = name
                self.counter = counter
            def run(self):
                print "Ready for connection"
                while running:
                    time.sleep(.2)              # sleep for 200 ms
            

        if __name__ == "__main__":
            running = True
        thread1 = myThread(1, "Thread-1", 1)
        thread1.setDaemon(True)
        thread1.start()
        application.listen(9093)          	#starts the websockets connection
        tornado.ioloop.IOLoop.instance().start()     
        
except KeyboardInterrupt:
	print "************* STOP  **************"
	FL.run(Raspi_MotorHAT.RELEASE)
	FR.run(Raspi_MotorHAT.RELEASE)
	BL.run(Raspi_MotorHAT.RELEASE)
	BR.run(Raspi_MotorHAT.RELEASE)
	time.sleep(1.0)
	pass

finally:
  sys.exit(0)

