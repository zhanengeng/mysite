"""epoll仅在linux里能用"""
from socket import *
import select

sSocket = socket(AF_INET, SOCK_STREAM)
sSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sSocket.bind(("",8080))
sSocket.listen(5)
epoll = select.epoll() #创建epoll对象

# 把套接字的文件描述符（fd）登记到epoll的事件监听中
epoll.register(sSocket.fileno(), select.EPOLLIN|select.EPOLLET)
#登记（监听套接字sSocket的文件描述符，是否是可读数据｜只通知一次）
# “|”是并集。EPOLLIN：是否可读(如果是客户端送信，则为可读)，EPOLLET：只通知一次。

connections = {}
addresses = {}

# 循环等待客户端的到来或对方发送数据
while True:
    epoll_list = epoll.poll() #以通知方式把收到的信息放入list。 功能上等价于select([],[],[])

    print(epoll_list)  #test

    #对检测到的套接字进行处理
    for fd, events in epoll_list: #文件描述符和EPOLLIN成对保存。
        if fd == sSocket.fileno(): #如果监听到的是链接请求
            print(f"客户端{cAddr}登陆.")
            cSocket, cAddr = sSocket.accept()

            #将cSocket的fd和address信息分别在字典中保存起来
            connections[cSocket.fileno()] = cSocket
            addresses[cAddr.fileno()] = cAddr

            # 像epoll中注册链接socket的可读事件
            epoll.register(cSocket.fileno(), select.EPOLLIN|select.EPOLLET)

        elif events == select.EPOLLIN: #如果得到可读数据（用户发信）

            #从字典中根据文件描述符(key)找到对应的套接字，再recv。
            getMsg = connections[fd].recv(1024)
            #connections[fd] = cSocket

            if getMsg:
                print(f">> {getMsg}")
            else:
                epoll.unregister(fd)
                connections[fd].close()
                print(f"{addresses[fd]}已下线.")