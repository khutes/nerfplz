from network import network
from config import network_config as cfg
from nerfCamera import client as camClient

cfg.init()

s = network.createCameraClient()

camClient.viewCameraFeed(s)