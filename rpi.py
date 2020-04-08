from network import network
from gpiozero import LED
from time import sleep
from nerfCamera import httpServer as camServ
from config import network_config as cfg
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


# We will want to remove this from a thread and let it run in the main thread
t = threading.Thread(target=camServ.startCameraFeed)
threads.append(t)
t.start()

# Move this block into a new module/thread before starting camera feed
while True:
    try:
        msg = msgSock.receive()
        if msg == "A Button Down":
            light.on()
        else:
            light.off()
        print(msg)
    except:
        cfg.ALIVE = False
        print("Error. Closing connection...")
        blinkLED(4)
        del msgSock
        break

for t in threads:
    t.join()
