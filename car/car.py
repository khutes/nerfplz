import RPi.GPIO as GPIO
from config import motor_config as mcfg
from car import motor
import time


class Car:
    motors = {}

    def __init__(self):
        # Add motors
        mcfg.init(self)
        self.firing = False
        self.motorsRunning = {}
        mList = list(self.motors.keys())
        for motor in mList:
            self.motorsRunning[motor] = False
        return

    def __del__(self):
        GPIO.cleanup()
        return

    def addDC(self, name, GPIOin1, GPIOin2, GPIOen, speed=10, minS=mcfg.DC_MIN_SPEED, maxS=mcfg.DC_MAX_SPEED):
        self.motors[name] = motor.DC(name, GPIOin1, GPIOin2, GPIOen, speed, minS, maxS)
        return

    def addServo(self, name, GPIOin, angle=90, minAngle=mcfg.SERVO_MIN_ANGLE, maxAngle=mcfg.SERVO_MAX_ANGLE, increment=mcfg.SERVO_ANGLE_INC):
        self.motors[name] = motor.Servo(name, GPIOin, angle, minAngle, maxAngle, increment)
        return

    def driveForward(self, factor):
        # Back motor forward
        if not self.motorsRunning["BackMotor"]:
            self.motorsRunning["BackMotor"] = True
            print("Called car.driveForward")
            self.motors["BackMotor"].fwd(factor)
        return

    def driveBackward(self, factor):
        # Back motor backward
        if not self.motorsRunning["BackMotor"]:
            self.motorsRunning["BackMotor"] = True
            # print("Called car.driveBackward")
            self.motors["BackMotor"].bckwd(factor)
        return

    def steerLeft(self, factor):
        # Front servo forwrad
        print("Called car.steerLeft")
        self.motors["FrontServo"].fwd(factor)
        return

    def steerRight(self, factor):
        # Front servo backward
        print("Called car.steerRight")
        self.motors["FrontServo"].bckwd(factor)
        return

    def lookLeft(self, factor):
        # Turret motor forward
        if not self.motorsRunning["TurretMotor"]:
            self.motorsRunning["TurretMotor"] = True
            print("Called car.lookLeft")
            self.motors["TurretMotor"].fwd(factor)
        return

    def lookRight(self, factor):
        # Turret motor backward
        if not self.motorsRunning["TurrretMotor"]:
            self.motorsRunning["TurretMotor"] = True
            print("Called car.lookRight")
            self.motors["TurretMotor"].bckwd(factor)
        return

    def lookUp(self, factor):
        # Tilt servo up
        # print("Called car.lookUp")
        self.motors["TiltServo"].fwd(factor)
        return

    def lookDown(self, factor):
        # Tilt servo down
        # print("Called car.lookDown")
        self.motors["TiltServo"].bckwd(factor)
        return

    def fire(self):
        # Fire motor
        if self.motorsRunning["FireMotor"]:
            self.motorsRunning["TurretMotor"] = False
            self.motors["FireMotor"].stop()
            time.sleep(1)
        else:
            print("Called car.fire")
            self.motorsRunning["FireMotor"] = True
            self.motors["FireMotor"].bckwd()
            time.sleep(1)
        return

    def stop(self, motor):
        if motor == "BackMotor" or motor == "TurretMotor":
            if self.motorsRunning[motor] == True:
                self.motors[motor].stop()
                self.motorsRunning[motor] = False
                print("Stopped " + str(motor))
        else:
            # print("Stopped " + str(motor))
            self.motors[motor].stop()
        return

    def reset(self):
        mList = list(self.motors.keys())
        for motor in mList:
            self.motors[motor].reset()
        return

    def printMotors(self):
        print(self.motors)
        return

