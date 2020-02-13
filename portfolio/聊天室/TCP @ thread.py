"""
这是一个TCP聊天室的客户端程序
因为多进程(Process)中input命令会产生EOFError，所以放弃多进程链接多客户端。
直接用多线程（Tread）收发消息。
问题点：input堵塞怎么破？
"""

from socket import *
# from multiprocessing import Pool
from threading import Thread
import time

# 从客户端接收信息
def recvMsg(cSocket, cAddr):
    global switch
    print(f"{cAddr}上线")
    while True:
        cMsg = cSocket.recv(1024).decode()
        # 结束通讯后关闭线程
        if len(cMsg) > 0:    #<--对方结束通话的标志
            print(f"\r>> {cAddr}: {cMsg}",end = "\n<< ")
        else:
            switch = False
            print(f"{cAddr}下线")
            # print("test:" + str(switch))  #switch == False  ok
            break

# 给客户端发信息
def sendMsg(cSocket, cAddr):
    global switch
    switch = True
    while True:
        try:
            send_msg = input("<< ")   #recvMsg结束时，input会堵塞！！！！
            cSocket.send(send_msg.encode())

        except EOFError as e:
            print(e)
            # break

        if switch == False:
            print("\n---test:结束sendMsg线程")  # ok
            break

switch = True #关闭线程循环的开关

def main():
    # 1.建立TCP服务器
    # 1.1 socket链接
    sSocket = socket(AF_INET, SOCK_STREAM)

    # 1.2 绑定地址
    sSocket.bind(("",8080))

    # 1.3 转为监听listen
    sSocket.listen(5)

    # print("---test1----")

    # 1.4 接受链接请求并在新进程中创建链接
    while True:
        cSocket, cAddr = sSocket.accept()
        # print("---test2----")   

        # 1.5 创建双线程，用于收/发信息  
        recv_thread = Thread(target=recvMsg,args=(cSocket, cAddr))
        send_thread = Thread(target=sendMsg,args=(cSocket, cAddr))
        recv_thread.start()
        send_thread.start()
        recv_thread.join() 
        send_thread.join()
        # print("---test3-----")  ok
        cSocket.close()  #通讯线程结束后，关闭cSocket。
        print("\n关闭用户的socket")

    # 关闭服务器套接字，应该不会用到
    # if xxx:
    #     sSocket.close()

if __name__ == "__main__":
    main()

