from time import sleep
import socket
from threading import Thread

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
serversocket.bind(("0.0.0.0", 8080))
# become a server socket
print(socket.gethostname())
serversocket.listen(1)

class CustomSocket:
    
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
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def receive(self):
        chunks = []
        bytes_recd = 0
        
        chunks.append(self.sock.recv(1).decode())
        MSGLEN = ''.join(chunks)
        while MSGLEN[-1] != "x":
            chunks.append(self.sock.recv(1).decode())
            MSGLEN = ''.join(chunks)
            
        MSGLEN = int(MSGLEN[:-1])
        chunks = []
            
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048)).decode()
            if chunk == '':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return ''.join(chunks)

def client_thread(socket, ip, port):
    s = CustomSocket(socket)
    while True:
        msg = s.receive()
        print(msg)

while True:
    # accept connections from outside
    (clientsocket, address) = serversocket.accept()
    # now do something with the clientsocket
    # in this case, we'll pretend this is a threaded server
    Thread(target=client_thread, args=(clientsocket, address[0], address[1])).start()
    