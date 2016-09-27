
#!/usr/bin/python3
# This is client.py file

import socket


class connection:
    def __init__(self, port, host, size):
        self.port = port
        self.host = host
        self.size = size

        # create a socket object
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connection to hostname on the port.
        self.socket.connect((self.host, self.port)) 

    def recive(self):
        msg = self.socket.recv(self.size)
        return msg.decode('ascii')

    def send(self, message):
        self.socket.send(message.encode('ascii'))

    def close(self):
        self.socket.close()

Erik = connection(9999, 'PowerBox', 1024) 

print(Erik.recive())
Erik.send("Hello World!")
Erik.close()
