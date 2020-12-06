from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('10.150.4.248', serverPort))
print('The server is ready to receive')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print('从客户主机收到信息：', message)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)