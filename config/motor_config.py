

DEFAULT_HERTZ = 50

DC_MAX_SPEED = 100
DC_MIN_SPEED = 0
DC_SPEED_INC = 5

# Default angle is 90
SERVO_MIN_ANGLE = 45
SERVO_MAX_ANGLE = 135
SERVO_ANGLE_INC = 1

# minAngle=55, maxAngle=125

def init(car):
    # name, in1, in2, ena, init speed, min speed, max speed
    car.addDC("BackMotor", GPIOin1=4, GPIOin2=27, GPIOen=22,
              speed=60, minS=15, maxS=75)  # Flipped directions

    # car.addDC("TurretMotor", GPIOin1=4, GPIOin2=27, GPIOen=22, speed=25, maxS=25)

    # car.addDC("FireMotor", GPIOin1=23, GPIOin2=24,
    #           GPIOen=18, speed=100, minS=15)

    # name, GPIO, init angle, min angle, max angle, increment
    # car.addServo("FrontServo", GPIOin=5, minAngle=45, maxAngle=135, increment=5)

    # car.addServo("TiltServo", GPIOin=17, minAngle=75, increment=5)

    car.printMotors()
    return
