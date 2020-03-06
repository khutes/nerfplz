import time
import socket
from threading import Thread

class Socket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

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


def createClient():

    # create an INET, STREAMing socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    mySocket = Socket(s)

    # hostname = socket.gethostname()
    # address = socket.gethostbyname(hostname)
    # print("Host Name: " + hostname + "\nAddress: " + address)

    piAddress = socket.gethostbyname("raspberrypi")
    # print("Pi Address: " + piAddress)

    mySocket.connect(piAddress, 8080)

    while True:
        msg = input("What message do you want to send?\n\nEnter: ")
        mySocket.send(msg)
        print("message sent\n")


def client_thread(socket, ip, port):
    s = Socket(socket)
    while True:
        try:
            msg = s.receive()
            print(msg)
        except:
            print("Error. Closing connection...")
            return


def createServer():
    # create an INET, STREAMing socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to a public host, and a well-known port
    serversocket.bind(("0.0.0.0", 8080))
    # become a server socket
    print(socket.gethostname())
    serversocket.listen(1)

    while True:
        # accept connections from outside
        (clientsocket, address) = serversocket.accept()
        # now do something with the clientsocket
        # in this case, we'll pretend this is a threaded server
        Thread(target=client_thread, args=(clientsocket, address[0], address[1])).start()
