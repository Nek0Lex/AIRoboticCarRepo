import time, atexit
import motorControl as car

atexit.register(car.turnOffMotors)


car.forward()
time.sleep(2)

car.left()
time.sleep(2)

car.backward()
time.sleep(2)

car.right()
time.sleep(2)

car.turnOffMotors()
time.sleep(2)


