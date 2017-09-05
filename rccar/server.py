from socket import *
import picamera
from time import sleep
import os

debug=True

class Server():
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.channel=socket(AF_INET,SOCK_STREAM)
        self.channel.bind((self.host,self.port))
        self.channel.listen(2)  #only 2 clients
        self.client,self.useless=self.server.accept()

    def stream(self,loc=None,timeout=2):
        self.camera = picamera.PiCamera()
        if not loc:
            loc=os.getcwd()
        while True:
            self.file = open(loc+'/image.jpg','wb')
            self.camera.capture(self.file)
            self.client.send(self.file.read())
            if debug:
                print("sent file\n")
            sleep(timeout)
