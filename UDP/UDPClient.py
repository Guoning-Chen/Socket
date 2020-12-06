from socket import *
serverName = '10.150.4.248'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print('从服务器主机收到信息：', modifiedMessage.decode())
clientSocket.close()