import RPi.GPIO as GPIO
from config import motor_config as mcfg

GPIO.setmode(GPIO.BCM)

class Motor:
    def __init__(self, name, GPIOin1, GPIOin2, GPIOen, speed):
        self.name = name
        self.in1 = GPIOin1
        self.in2 = GPIOin2
        self.en = GPIOen
        self.speed = speed

        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.en, GPIO.OUT)
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        self.p = GPIO.PWM(self.en, mcfg.DEFAULT_HERTZ)
        self.p.start(self.speed)
        return

    def __del__(self):
        self.p.stop()

    def fwd(self, speed=None):
        if speed is not None:
            self.setSpeed(speed)
        self.p.ChangeDutyCycle(self.speed)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in1, GPIO.HIGH)
        return

    def bckwd(self, speed=None):
        if speed is not None:
            self.setSpeed(speed)
        self.p.ChangeDutyCycle(self.speed)
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        return

    def setSpeed(self, speed):
        self.speed = speed
        if self.speed > 90:
            self.speed = 90
        elif self.speed < 0:
            self.speed = 0
        print("%s speed set to %f", self.name, self.speed) 
        return

    def stop(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        return
