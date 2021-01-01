from socket import *
import time

serverName = '10.150.4.248'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)  # IPv4，数据报格式
clientSocket.settimeout(1)  # 设置超时等待时间 1s
rtt = []
count = 0
for i in range(10):  # 10个ping
    time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    message = "Ping %d %s" % (i + 1, time_stamp)
    modifiedMessage = None
    serverAddress = None
    start_time = int(round(time.time() * 1E6))  # 微秒级别
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        end_time = int(round(time.time() * 1E6))
        dif = end_time - start_time
        rtt.append(dif)
        print('%0d: %s, RTT: %.1fus' % (i+1, modifiedMessage.decode(), dif))
    except:
        print("%0d: Request timed out" % (i+1))
        count += 1
clientSocket.close()
rtt_sum = 0
for r in rtt:
    rtt_sum += r
print("rtt: max %.1fus, min %.1fus, average %.1fus" % (max(rtt), min(rtt),
                                                       rtt_sum / count))
print("packet loss rate: %.2f%%" % (count / 10 * 100))
