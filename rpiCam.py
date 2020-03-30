from network import network
from nerfCamera import server as camServ

c = network.createCameraServer()

camServ.startCameraFeed(c)
