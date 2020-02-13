from socket import *
 
"""创建TCP server"""
 
# 1.创建套接字（作用是等待呼叫）
serverSocket = socket(AF_INET, SOCK_STREAM) #TCP
 
# 2.绑定ip和port（服务器固定，并为接收方，所以绑定）
serverSocket.bind(("",8080))
 
# 3.把socket变成被动监听。
print("---test--转入监听模式---")
serverSocket.listen(5)  #（括号里是最大时能接受客户端数目，随便写。）
 
# 4.接受呼叫并分配线路,若无来电，则程序在此处堵塞
clientSocket, clientAddr = serverSocket.accept() #accept的返回值为元祖(socket,(ip,port))。
#clientSocket:为此客户端服务的套接字，clientAddr:（来电显示得到的）客户端地址。

print("---test--建立连接---")
 
# 5.收发数据(recv/send)
recvData = clientSocket.recv(1024).decode()  #收发数据要解码。
print("---test--收到以下信息---")
 
print(f"{str(clientAddr)}来信: {recvData}")

send_msg = input("发送测试: ").encode()
clientSocket.send(send_msg)
print("succeed!")
 
clientSocket.close()
serverSocket.close()
 
# ---test--转入监听模式---
# ---test--建立连接---
# ---test--收到以下信息---
# ('192.168.0.11', 59907)来信: Send from TCP/UDP Assistant on my windows
