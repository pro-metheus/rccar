from socket import *
import picamera
from time import sleep
import os
debug=True



class Client():
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.channel=socket(AF_INET,SOCK_STREAM)
        self.client,self.useless=self.channel.connect((self.host,self.port))

    def rec(self,loc=None):
        if not loc:
            loc=os.getcwd()
        while True:
            self.file = open(loc+'/image.jpg','rb')
            self.data=self.client.recv(1024)
            if debug:
                print("recieved\n")
            self.file.write(self.data)
