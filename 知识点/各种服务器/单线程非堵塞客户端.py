"""单进程非堵塞服务器"""
"""少数客户端时和多线程无明显区别，多客户端时处理速度变慢"""
from socket import *
import time

sSocket = socket(AF_INET, SOCK_STREAM)
sSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)  #端口释放
sSocket.bind(("",8080))
sSocket.listen(10)
sSocket.setblocking(False) #防止sSocket.accept()堵塞

clientList=[]  #用来储存已连接的客户端，实现多连效果

while True:
    #等待新客户端到来（即完成3次握手的客户端）
    try:
        cSocket,cAddr = sSocket.accept()    
        time.sleep(0.2)   #节约cpu
    except:
        pass
    else:
        print(f"{cAddr}已上线。")
        clientList.append((cSocket, cAddr))
        cSocket.setblocking(False) #防止cSocket.recv()堵塞

    for cSocket, cAddr in clientList:
        try:
            getMsg = cSocket.recv(1024).decode()
        except:
            pass
        else:
            if getMsg:
                print(f"{cAddr}: {getMsg}")
            else:
                print(f"{cAddr}已下线。")
                clientList.remove((cSocket, cAddr))
                cSocket.close()
        
