#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverPort = 12000
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  #Fill
    try:
        message = connectionSocket.recv(1024)  #Fill
        filename = message.split()[1]
        f = open(filename[1:])
        outputData = f.readline()  #Fill
        #Send one HTTP header line into socket
        #Fill in start
        # f = open(s.decode('ascii'), 'r', encoding='UTF-8')
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputData)):
            connectionSocket.send(outputData[i])
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        connectionSocket.send(b'404 Not Found')
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end
serverSocket.close()