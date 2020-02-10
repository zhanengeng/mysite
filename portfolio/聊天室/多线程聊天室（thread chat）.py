from socket import *    
from threading import Thread

def recvMsg():
    while True:
        #接收信息
        recv_msg = udpsocket.recvfrom(1024) 
        #解码并打印消息
        msg = recv_msg[0].decode("utf-8")
        print(f">>({recv_msg[1]}): {msg}")  
        print("-----test--recvMsg-----")

def sendMsg():
    while True:
        # 发送信息
        send_msg = input("<<")
        udpsocket.sendto(send_msg.encode("utf-8"), (destIp, destPort))
        print("-----test--sedMsg-----")

udpsocket = None
destIp = ""
destPort = 0

def main():
    global udpsocket, destIp, destPort
    # 创建套接字
    udpsocket = socket(AF_INET, SOCK_DGRAM)
    # 绑定本地信息(ip,port)
    udpsocket.bind(("",1234))
    # 获取对方信息
    destIp = input("对方IP: ")
    destPort = int(input("对方端口: "))

    #创建多线程         
    thread1 = Thread(target=recvMsg)
    thread2 = Thread(target=sendMsg)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print("-----test--end-----")

if __name__ == "__main__":
    main()
