from network import network
from gpiozero import LED
from time import sleep
from nerfCamera import server as camServ
import threading

threads = []

light = LED(12)

# Creating the camera server is currently a blocking function until a connection is established
camSock = network.createCameraServer()
msgSock = network.createMessageServer()

t = threading.Thread(target=camServ.startCameraFeed, args=(camSock,))
threads.append(t)
t.start()

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
