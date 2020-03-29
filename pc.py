from config import network_config as cfg
from network import network
from network import ssh
import time
import threading

threads = []

while True:
    try:
        cfg.init()
        break
    except Exception as e:
        print("Error obtaining raspberry pi address. Retrying in 5 seconds...")
        time.sleep(5)

while True:
    try:
        ssh.execute()
        break
    except Exception as e:
        print("Error starting server on raspberry pi. Retrying in 5 seconds...")
        time.sleep(5)

try:
    t = threading.Thread(target=network.createCameraClient)
    threads.append(t)
    network.createMessageClient()
except Exception as e:
    print("Error operating client: " + str(e))
    print("Shutting down system...")

for t in threads:
    t.join()
    
# This option exists if we want to kill the server forcibly from the pc
# Currently it should all be handled from the rpi 
# try:
#     ssh.killServer()
# except Exception as e:
#     print("Error killing server on RPI\nWARNING: Processes may still be running on RPI")
