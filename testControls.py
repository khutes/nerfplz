#This program detects input from the controller and prints it to the screen.
#Next step, each input will call a specific function that controls the motors.
#Integrate this with networking and camera
import pygame
import time
from car import car

keyDelay = .01

def run(car):
    selM = car.motors[list(car.motors.keys())[0]]
    pygame.init()
    done = False
    # Creates a pygame screen, be sure to click on the screen to use it
    screen = pygame.display.set_mode((100, 100))
    try:
        while done == False:
            # event handling
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                selM.fwd()
                time.sleep(keyDelay)
            if keys[pygame.K_s]:
                selM.bckwd()
                time.sleep(keyDelay)
            if keys[pygame.K_m]:
                selM.stop()
                car.printMotors()
                selM = car.motors[input("Select a new motor: ")]
                time.sleep(keyDelay)
            if keys[pygame.K_UP]:
                selM.setSpeed(selM.speed + selM.increment)
                time.sleep(keyDelay)
            if keys[pygame.K_DOWN]:
                selM.setSpeed(selM.speed - selM.increment)
                time.sleep(keyDelay)
            if keys[pygame.K_SPACE]:
                selM.stop()
                time.sleep(keyDelay)
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    del car
                    done = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        selM.stop()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        selM.stop()

    except KeyboardInterrupt:
        del car
        pygame.quit()

car = car.Car()

run(car)