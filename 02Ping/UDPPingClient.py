from socket import *
import time

serverName = '10.150.4.248'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)  # IPv4，数据报格式
clientSocket.settimeout(1)  # 设置超时等待时间 1s
for i in range(10):  # 10个ping
    time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    message = "Ping %d %s" % (i, time_stamp)
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage = None
    serverAddress = None
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print('从服务器主机收到信息：', modifiedMessage.decode())
    except:
        print("Request timed out")
clientSocket.close()