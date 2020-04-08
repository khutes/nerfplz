

DEFAULT_HERTZ = 50
DEFAULT_MAX_SPEED = 90
DEFAULT_MIN_SPEED = 25


def init(car):
    car.addMotor(
        "test",
        24,
        23,
        25,
        50
    )
    # Add motors here as desired
    car.printMotors()
    return
