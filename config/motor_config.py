

DEFAULT_HERTZ = 50

DC_MAX_SPEED = 100
DC_MIN_SPEED = 0
DC_SPEED_INC = 5

# Default angle is 90
SERVO_MIN_ANGLE = 45
SERVO_MAX_ANGLE = 135
SERVO_ANGLE_INC = 1

def init(car):
    # name, in1, in2, ena, init speed, min speed, max speed
    car.addDC("BackMotor", 16, 20, 21, 40, 15, 100) # Flipped directions
    car.addDC("TurretMotor", 19, 13, 26, 15)
    car.addDC("FireMotor", 6, 5, 14, 50, 15, 75)

    # name, GPIO, init angle, min angle, max angle, increment
    car.addServo("FrontServo", 17, minAngle=55, maxAngle=125, increment=5)
    car.addServo("TiltServo", 27, minAngle=75)

    car.printMotors()
    return
