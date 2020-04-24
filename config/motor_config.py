

DEFAULT_HERTZ = 50

DC_MAX_SPEED = 50
DC_MIN_SPEED = 10
DC_SPEED_INC = 1

SERVO_MIN_ANGLE = 45
SERVO_MAX_ANGLE = 135
SERVO_ANGLE_INC = 1

def init(car):
    car.addDC("BackMotor", 23, 24, 25, 30)
    car.addServo("FrontServo", 17, 90)
    # Add motors here as desired
    car.printMotors()
    return
