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
    sleep(1)
    return

# Creating the camera server is currently a blocking function until a connection is established
camSock = network.createCameraServer()
msgSock = network.createMessageServer()

t = threading.Thread(target=camServ.startCameraFeed, args=(camSock,))
threads.append(t)
t.start()

while True:
    try:
        msg = msgSock.receive()
        if msg == "1":
            light.on()
        elif msg == "0":
            light.off()
        print(msg)
    except:
        print("Error. Closing connection...")
        blink(4)
        del s
        break

for t in threads:
    t.join()
