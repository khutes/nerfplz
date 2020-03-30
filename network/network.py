import time
import socket
from threading import Thread
from config import network_config as cfg

class Socket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET6, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def __del__(self):
        self.sock.close()

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, msg):
        totalsent = 0
        MSGLEN = len(msg)
        msg = str(MSGLEN) + "x" + msg
        msg = msg.encode()
        MSGLEN = len(msg)
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def receive(self):
        chunks = []
        bytes_recd = 0

        chunk = self.sock.recv(1).decode()
        if chunk == '':
            raise RuntimeError("socket connection broken")

        chunks.append(chunk)
        MSGLEN = ''.join(chunks)

        while MSGLEN[-1] != "x":
            chunks.append(self.sock.recv(1).decode())
            MSGLEN = ''.join(chunks)

        MSGLEN = int(MSGLEN[:-1])
        chunks = []

        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048)).decode()
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return ''.join(chunks)


def __createClient(port):

    # create an INET, STREAMing socket
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

    mySocket = Socket(s)

    piAddress = cfg.HOST
    piPort = port

    mySocket.connect(piAddress, piPort)

    if (port == cfg.MESSAGE_PORT):
        while True:
            try:
                msg = input("Enter Message: ")
                if msg == "quit":
                    print("Closing client...")
                    del mySocket
                    cfg.ALIVE = False
                    break
                mySocket.send(msg)
                print("message sent\n")
            except:
                cfg.ALIVE = False
                print("Send error. Closing connection...")
                break
        return
    else:
        return mySocket

def createMessageClient():
    return __createClient(cfg.MESSAGE_PORT)

def createCameraClient():
    return __createClient(cfg.CAMERA_PORT)

def __createServer(port):
    # create an INET, STREAMing socket
    serversocket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    # bind the socket to a public host, and a well-known port
    serversocket.bind(("::", port))
    # become a server socket
    print(socket.gethostname())
    serversocket.listen(1)

    # accept 1 connection from outside
    (clientsocket, address) = serversocket.accept()
    # now do something with the clientsocket
    # Thread(target=client_thread, args=(clientsocket, address[0], address[1]), daemon=True).start()
    s = Socket(clientsocket)
    return s

def createMessageServer():
    return __createServer(cfg.MESSAGE_PORT)

def createCameraServer():
    return __createServer(cfg.CAMERA_PORT)
        
