from network import network
from gpiozero import LED
from time import sleep

light = LED(12)

s = network.createServer()

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
