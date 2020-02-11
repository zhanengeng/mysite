from socket import *    
from threading import Thread

def recvMsg():
    while True:
        #接收信息
        recv_msg = udpsocket.recvfrom(1024) 
        #解码并打印消息
        msg = recv_msg[0].decode("utf-8")
        print(f"\r>>{recv_msg[1]}: {msg}",end="\n<<")  
        # print("-----test--recvMsg-----")

def sendMsg():
    while True:
        # 发送信息
        send_msg = input("<< ")
        udpsocket.sendto(send_msg.encode("utf-8"), (destIp, destPort))
        # print("-----test--sedMsg-----")

def get_host_ip(udpsocket):
    """查询本机ip地址.return: ip"""
    try:
        udpsocket.connect(('8.8.8.8', 80))
        ip = udpsocket.getsockname()[0]
    finally:
        udpsocket.close()
    return ip

udpsocket = None
destIp = ""
destPort = 0

def main():
    global udpsocket, destIp, destPort
    # 创建套接字
    udpsocket = socket(AF_INET, SOCK_DGRAM)
    # 绑定本地信息(ip,port)——
    test_port = 1234           #test_port信息可在1024~65535间随意设定
    udpsocket.bind(("",test_port))  
    # 获取对方信息
    # hostname = gethostname()
    hostip = get_host_ip(udpsocket)
    destIp = input(f"对方IP(测试用本机IP:{hostip}): ")
    destPort = int(input(f"对方端口(测试用端口:{test_port}): "))

    #创建多线程         
    thread1 = Thread(target=recvMsg)
    thread2 = Thread(target=sendMsg)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    # print("-----test--end-----")

if __name__ == "__main__":
    main()