from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import carSpeed as speed

# create a default object, no changes to I2C address or frequency
mh = Raspi_MotorHAT(addr=0x6f)

# Objects for 4 wheels
FL = mh.getMotor(4)
FR = mh.getMotor(3)
BL = mh.getMotor(2)
BR = mh.getMotor(1)

speed_FL = speed.speed_FL
speed_FR = speed.speed_FR
speed_BL = speed.speed_BL
speed_BR = speed.speed_BR

turningSpeed = speed.turningAngle
blast = speed.blastingSpeed

def turnOffMotors():
    print "Turn OFF ALL motors!  "
    FL.run(Raspi_MotorHAT.RELEASE)
    FR.run(Raspi_MotorHAT.RELEASE)
    BL.run(Raspi_MotorHAT.RELEASE)
    BR.run(Raspi_MotorHAT.RELEASE)

def magic():
        print "Magic Power!  "
        FL.setSpeed(speed_FL+blast)
        FR.setSpeed(speed_FR+blast)
        BL.setSpeed(speed_BL+blast)
        BR.setSpeed(speed_BR+blast)

        FL.run(Raspi_MotorHAT.FORWARD)
        FR.run(Raspi_MotorHAT.FORWARD)
        BL.run(Raspi_MotorHAT.FORWARD)
        BR.run(Raspi_MotorHAT.FORWARD)

def forward():
        print "Forward!  "
        FL.setSpeed(speed_FL)
        FR.setSpeed(speed_FR)
        BL.setSpeed(speed_BL)
        BR.setSpeed(speed_BR)

        FL.run(Raspi_MotorHAT.FORWARD)
        FR.run(Raspi_MotorHAT.FORWARD)
        BL.run(Raspi_MotorHAT.FORWARD)
        BR.run(Raspi_MotorHAT.FORWARD)
    
def backward():
        print "Backward!  "
        FL.setSpeed(speed_FL)
        FR.setSpeed(speed_FR)
        BL.setSpeed(speed_BL)
        BR.setSpeed(speed_BR)

        FL.run(Raspi_MotorHAT.BACKWARD)
        FR.run(Raspi_MotorHAT.BACKWARD)
        BL.run(Raspi_MotorHAT.BACKWARD)
        BR.run(Raspi_MotorHAT.BACKWARD)

def left():
        print "Turn Left!  "
        FL.setSpeed(speed_FL - turningSpeed)
        FR.setSpeed(speed_FR + turningSpeed)
        BL.setSpeed(speed_BL - turningSpeed)
        BR.setSpeed(speed_BR + turningSpeed)

        FL.run(Raspi_MotorHAT.FORWARD)
        FR.run(Raspi_MotorHAT.FORWARD)
        BL.run(Raspi_MotorHAT.FORWARD)
        BR.run(Raspi_MotorHAT.FORWARD)


def right():
        print "Turn Right!  "
        FL.setSpeed(speed_FL + turningSpeed)
        FR.setSpeed(speed_FR - turningSpeed)
        BL.setSpeed(speed_BL + turningSpeed)
        BR.setSpeed(speed_BR - turningSpeed)

        FL.run(Raspi_MotorHAT.FORWARD)
        FR.run(Raspi_MotorHAT.FORWARD)
        BL.run(Raspi_MotorHAT.FORWARD)
        BR.run(Raspi_MotorHAT.FORWARD)