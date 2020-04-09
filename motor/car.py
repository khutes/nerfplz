import RPi.GPIO as GPIO
from motor import motor_config as mcfg
from motor import motor

class Car:
    motors = {}

    def __init__(self):
        # Add motors
        mcfg.init(self)
        return

    def __del__(self):
        GPIO.cleanup()
        return

    def addDC(self, name, GPIOin1, GPIOin2, GPIOen, speed=10):
        self.motors[name] = motor.DC(name, GPIOin1, GPIOin2, GPIOen, speed)
        return

    def addServo(self, name, GPIOin, speed=10):
        self.motors[name] = motor.Servo(name, GPIOin, speed=2.5)
        return

    def driveForward(self, factor):
        # Back motor forward
        print("Called car.driveForward")
        self.motors["dc1"].fwd()
        return

    def driveBackward(self, factor):
        # Back motor backward
        print("Called car.driveBackward")
        self.motors["dc1"].bckwd()
        return

    def steerLeft(self, factor):
        # Front servo forwrad
        print("Called car.steerLeft")
        return

    def steerRight(self, factor):
        # Front servo backward
        print("Called car.steerRight")
        return

    def lookLeft(self, factor):
        # Turret servo forward
        print("Called car.lookLeft")
        return

    def lookRight(self, factor):
        # Turret servo backward
        print("Called car.lookRight")
        return

    def lookUp(self, factor):
        # Tilt servo up
        print("Called car.lookUp")
        return

    def lookDown(self, fact0r):
        # Tilt servo down
        print("Called car.lookDown")
        return

    def fire(self):
        # Fire motor
        print("Called car.fire")
        return

    def stop(self):
        self.motors["dc1"].stop()
        return

    def printMotors(self):
        print(self.motors)
        return

