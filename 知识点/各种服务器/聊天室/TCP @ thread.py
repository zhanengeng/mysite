"""
这是一个TCP聊天室的客户端程序
因为多进程(Process)中input命令会产生EOFError，所以放弃多进程链接多客户端。
直接用多线程（Tread）收发消息。
问题点：input堵塞怎么破？
"""

from socket import *
# from multiprocessing import Pool
from threading import Thread, Lock
import time

# 从客户端接收信息
def recvMsg(cSocket, cAddr, lock):
    global switch
    print(f"{cAddr}上线")
    while True:
        try:
            cMsg = cSocket.recv(1024).decode()
        except:
            pass
        else:
            # 结束通讯后关闭线程
            if len(cMsg) > 0:    #<--对方结束通话的标志
                print(f"\r>> {cAddr}: {cMsg}",end = "\n<< ")
            else:
                print(f"{cAddr}下线")
                switch = 1
                print("test: switch=" + str(switch))  #switch == False  ok
                time.sleep(1)
                break
    
    # if switch == 0:
# 
# 给客户端发信息
def sendMsg(cSocket, cAddr, lock):
    global switch
    switch = 0
    while True:
        try:
            send_msg = input("<< ")   #recvMsg结束时，input会堵塞！！！！
            # send_msg = "test,test,test"
            # time.sleep(1)
            cSocket.send(send_msg.encode())

        except:
            pass

        if switch == 1:
            print("---test:结束sendMsg线程")
            # switch = 0 #结束socket开关
            # print("---test:switch==0")
            break
    cSocket.close()  #通讯线程结束后，关闭cSocket。
    print("关闭用户的socket")

switch = 0 #关闭线程循环的开关

def main():
    # 1.建立TCP服务器
    # 1.1 socket链接
    sSocket = socket(AF_INET, SOCK_STREAM)
    sSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #服务器意外中断时，充值端口绑定
    lock = Lock()

    # 1.2 绑定地址
    sSocket.bind(("",8080))

    # 1.3 转为监听listen
    sSocket.listen(5)

    # print("---test1----")

    # 1.4 接受链接请求并在新进程中创建链接
    while True:
        cSocket, cAddr = sSocket.accept()
        cSocket.setblocking(False)  #解决input堵塞,未成功。
        # print("---test2----")   

        # 1.5 创建双线程，用于收/发信息  
        recv_thread = Thread(target=recvMsg,args=(cSocket, cAddr, lock))
        send_thread = Thread(target=sendMsg,args=(cSocket, cAddr, lock))
        recv_thread.start()
        send_thread.start()
    
        # print("---test3-----")  ok

    # 关闭服务器套接字，应该不会用到
    # if xxx:
    #     sSocket.close()

if __name__ == "__main__":
    main()

