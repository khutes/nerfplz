import network
from gpiozero import LED

light = LED(12)

network.Socket s = network.createServer()

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
        break
