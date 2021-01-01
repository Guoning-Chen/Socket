#可选练习一较简单，故略过
from socket import *
import time

serverName = '10.150.4.248'
serverPort = 800
clientSocket=socket(AF_INET,SOCK_DGRAM)
for i in range(10):
    send_time = time.time()
    message = str(i + 1) + ' ' + str(time.time())
    clientSocket.sendto(message.encode(), (serverName, serverPort))
clientSocket.close()
