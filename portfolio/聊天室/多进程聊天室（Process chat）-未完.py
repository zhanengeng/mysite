from socket import *    
from multiprocessing import Pool  
import time 

def recvMsg():
    while True:
        #接收信息
        recv_msg = udpsocket.recvfrom(1024) 
        #解码并打印消息
        msg = recv_msg[0].decode("utf-8")
        print(f">>({recv_msg[1]}): {msg}")  
        print("-----test--recvMsg-----")
        time.sleep(0.2)

def sendMsg():
    while True:
        # 发送信息
        send_msg = input("<<")
        udpsocket.sendto(send_msg.encode("utf-8"), (destIp, destPort))
        print("-----test--sedMsg-----")
        time.sleep(0.2)

def main():
    # 创建套接字
    udpsocket = socket(AF_INET, SOCK_DGRAM)
    # 绑定本地信息(ip,port)
    udpsocket.bind(("",1234))
    # 获取对方信息
    destIp = input("对方IP: ")
    destPort = int(input("对方端口: "))

    #创建多进程         
    pool = Pool()
    pool.apply_async(recvMsg)
    pool.apply_async(sendMsg)
    pool.close()
    pool.join()
    print("-----test--end-----")

if __name__ == "__main__":
    main()

