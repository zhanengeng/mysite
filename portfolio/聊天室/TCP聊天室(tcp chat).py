"""
这是一个TCP聊天室的客户端程序
利用了多线程(Process)链接客户端，并用多进程（Tread）收发消息。
"""

from socket import *
from multiprocessing import Pool
from threading import Thread
import time

def clientConnect(cSocket, cAddr):
# 1.5 创建双线程，用于收/发信息  
    recv_thread = Thread(target=recvMsg,args=(cSocket, cAddr))
    send_thread = Thread(target=sendMsg,args=(cSocket, cAddr))
    recv_thread.start()
    send_thread.start()
    recv_thread.join() 
    send_thread.join()
    # print("---test3-----")  ok
    cSocket.close()  #通讯线程结束后，关闭cSocket。
    print("结束用户的socket")

# 从客户端接收信息
def recvMsg(cSocket, cAddr):
    global switch
    print(f"{cAddr}已上线")
    while True:
        getMsg = cSocket.recv(1024).decode()
        # 结束通讯后关闭线程
        if getMsg:    #<-- len(getMsg)== 0 则对方结束通话
            print(f"\r>> {cAddr}: {getMsg}",end = "\n<< ")
        else:
            switch = False
            print(f"{cAddr}下线")
            break

# 给客户端发信息
def sendMsg(cSocket, cAddr):
    global switch
    switch = True
    while True:
        try:
            send_msg = input("<< ")   #input会堵塞，想想怎么破
            # print("---test4---")
            cSocket.send(send_msg.encode())
        except EOFError as e:
            print(e)
            # break
        # 上面这段代码有问题，未来解决
        # cSocket.send("----test-sendMsg----".encode())   #这句是测试用代码，EOFError解决后删掉。
        # time.sleep(1)

        if switch == False:  #用于在收信线程结束后，终止发信线程
            print("---test: 结束sendMsg线程")  #ok
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
        newProcess = Pool(5)
        newProcess.apply_async(clientConnect,(cSocket, cAddr))

    # 关闭服务器套接字，应该不会用到
    # if xxx:
    #     sSocket.close()

if __name__ == "__main__":
    main()





