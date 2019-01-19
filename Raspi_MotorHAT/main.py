from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

import keyboard
import time
import atexit

##config speed of motor
mh = Raspi_MotorHAT(addr=0x6f)
speed_FL = 60
Speed_FR = 60
Speed_BL = 60
Speed_BR = 60

##init the motor 
FL = mh.getMotor(4)
FR = mh.getMotor(3)
BL = mh.getMotor(2)
BR = mh.getMotor(1)

##auto-disabling motors on shutdown
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
        
##set speed of wheel
FL.setSpeed(speed_FL)
FR.setSpeed(Speed_FR)
BL.setSpeed(Speed_BL)
BR.setSpeed(Speed_BR)

# turn on motor
FL.run(Raspi_MotorHAT.RELEASE)
FR.run(Raspi_MotorHAT.RELEASE)
BL.run(Raspi_MotorHAT.RELEASE)
BR.run(Raspi_MotorHAT.RELEASE)

##main
print('wasd control, q for stop')
while True:
    #direction = raw_input("Please enter direction: ")
    if keyboard.is_pressed('w'):
        while True:
            FL.run(Raspi_MotorHAT.FORWARD)
            FR.run(Raspi_MotorHAT.FORWARD)
            BL.run(Raspi_MotorHAT.FORWARD)
            BR.run(Raspi_MotorHAT.FORWARD)
            if keyboard.is_pressed('q'):
                turnOffMotors()
                break;
            
    if keyboard.is_pressed('s'):
        while True:
            FL.run(Raspi_MotorHAT.BACKWARD)
            FR.run(Raspi_MotorHAT.BACKWARD)
            BL.run(Raspi_MotorHAT.BACKWARD)
            BR.run(Raspi_MotorHAT.BACKWARD)
            if keyboard.is_pressed('q'):
                turnOffMotors()
                break;
    
