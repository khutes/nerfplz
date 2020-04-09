from network import network
from gpiozero import LED
from time import sleep
from nerfCamera import httpServer as camServ
from config import network_config as cfg
from config import message_parser as receive_from_pc
from motor import car
import threading

threads = []

light = LED(12)

def blinkLED(numTimes):
    for i in range(numTimes):
        light.on()
        sleep(.25)
        light.off()
        sleep(.25)
    sleep(1)
    return

# Creating the camera server is currently a blocking function until a connection is established
# camSock = network.createCameraServer()
msgSock = network.createMessageServer()
car = car.Car()

t = threading.Thread(target=receive_from_pc.parse, args=(msgSock, car,))
threads.append(t)
t.start()

# We will want to remove this from a thread and let it run in the main thread
# t = threading.Thread(target=camServ.startCameraFeed)
# threads.append(t)
# t.start()

for t in threads:
    t.join()
