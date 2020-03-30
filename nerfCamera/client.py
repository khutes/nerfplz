import io
import socket
import struct
from PIL import Image
import matplotlib.pyplot as pl
from config import network_config as cfg

def viewCameraFeed(cameraSocket):
    # Accept a single connection and make a file-like object out of it
    # connection = cameraSocket.accept()[0].makefile('rb')
    connection = cameraSocket.sock.makefile('rb')
    try:
        img = None
        while cfg.ALIVE:
            # Read the length of the image as a 32-bit unsigned int. If the
            # length is zero, quit the loop
            image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
            if not image_len:
                break
            # Construct a stream to hold the image data and read the image
            # data from the connection
            image_stream = io.BytesIO()
            image_stream.write(connection.read(image_len))
            # Rewind the stream, open it as an image with PIL and do some
            # processing on it
            image_stream.seek(0)
            image = Image.open(image_stream)
            
            if img is None:
                img = pl.imshow(image)
            else:
                img.set_data(image)

            pl.pause(0.01)
            pl.draw()

            # print('Image is %dx%d' % image.size)
            image.verify()
            # print('Image is verified')
    finally:
        connection.close()

    return