from network import network
from network import message_parser as parser
from time import sleep
from config import network_config as cfg
from car import car
from nerfCamera import httpServer as camServ
import threading

threads = []

msgSock = network.createMessageServer()
car = car.Car()

t = threading.Thread(target=parser.parse, args=(msgSock, car,))
threads.append(t)
t.start()

# We will want to remove this from a thread and let it run in the main thread
camServ.startCameraFeed()
# t = threading.Thread(target=camServ.startCameraFeed)
# threads.append(t)
# t.start()

for t in threads:
    t.join()
