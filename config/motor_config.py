

DEFAULT_HERTZ = 50

DC_MAX_SPEED = 100
DC_MIN_SPEED = 0
DC_SPEED_INC = 5

# Default angle is 90
SERVO_MIN_ANGLE = 45
SERVO_MAX_ANGLE = 135
SERVO_ANGLE_INC = 1

def init(car):
    car.addDC("BackMotor", 16, 20, 21, 40)
    car.addDC("TurretMotor", 19, 26, 13, 15)
    car.addDC("FireMotor", 5, 11, 6, 50)

    car.addServo("FrontServo", 17)
    car.addServo("TiltServo", 27)

    car.printMotors()
    return
