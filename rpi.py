from network import network
from gpiozero import LED
from time import sleep
from nerfCamera import server as camServ
import threading

threads = []

light = LED(12)

def blinkLED(numTimes):
    for i in range(numTimes):
        light.on()
        sleep(.25)
        light.off()
        sleep(.25)
    return

# Creating the camera server is currently a blocking function until a connection is established
camSock = network.createCameraServer()
blinkLED(1)
msgSock = network.createMessageServer()
blinkLED(2)

t = threading.Thread(target=camServ.startCameraFeed, args=(camSock,))
threads.append(t)
t.start()
blinkLED(3)

while True:
    try:
        msg = s.receive()
        if msg == "1":
            light.on()
        elif msg == "0":
            light.off()
        print(msg)
    except:
        print("Error. Closing connection...")
        for i in range(4):
            light.on()
            sleep(.25)
            light.off()
            sleep(.25)
        del s
        break

for t in threads:
    t.join()
