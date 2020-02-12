from socket import *
import struct
import os
"""
操作码: opCode
块编号: blcNum
ip+port: serverInfo
信息内容: recvPacket（opCode+blcNum+data）
通讯请求: requestFileDate
"""
def main():
        
    filename = input("下载文件的名字(如test.jpg): ").encode()
    
    # 导入socket
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    # 绑定接受地址，不绑也行，作为主动发送方，不必知道自己port。服务器有来电显示（笑）
    # udpSocket.bind("",1234)

    # 创建下载请求
    requestFileDate = struct.pack(f"!H{len(filename)}sb5sb",1,filename,0,"octet".encode(),0)   #pack：组包，多字节表示一个值时需要用到。“!”代表了用网络传输，也就是大端。H占两个字节的坑，5s:5字符，b：1字节。
    # 发送请求
    udpSocket.sendto(requestFileDate ,("192.168.0.11",69))

    #在本地创建一个空文件
    f = open(filename,"bw")  #bw可以写入文字以外的信息。如图片。
    num = 0          #验证块编号用
    flag = False      #验证下载成功与否

    while True:
        # 接受服务器反馈数据包(讯息,(IP,port))
        recvPacket = udpSocket.recvfrom(1024) 
        # 把数据包拆分成讯息与地址（数据包 = (讯息，(ip，port))）
        recvPacket, serverInfo = recvPacket
        # 把讯息拆分并获取操作码(opCode)与块编号(blcNum)  (讯息 == "操作码 + 块编号 + 数据内容")
        opCode, blcNum = struct.unpack("!HH",recvPacket[:4])  #unpack后返回的是元祖(操作码，块编号)。
        # 取得下载数据内容(data)
        data = recvPacket[4:]

        # 若数据包正确（cmd==3），保存数据，并给server返回ACK
        if opCode == 3:
            num += 1
            if num == blcNum:   #判断块编号正确性
                # 给空文件写入数据
                f.write(data)
                if num%300 == 100:
                    print("\r传输中.",end="")
                elif num%300 == 200:
                    print("\r传输中..",end="")
                elif num%300 == 0:
                    print("\r传输中...",end="")

            # 组包ACK（操作码+块编号）
            ackData = struct.pack("!HH", 4, blcNum)
            # 发送ACK(ack编号,(ip+port))
            udpSocket.sendto(ackData,serverInfo)

            # 当收到讯息总长度小于516，则证明传输结束
            if len(recvPacket) < 516:
                print("\n下载成功!")
                f.close()
                flag = True
                break

        # 若数据包错误（cmd==5）
        elif opCode == 5:
            print("传输未成功！")
            break
        
    if flag == False:
        os.remove(filename)

    # 关闭套接字
    udpSocket.close()

if __name__ == "__main__":
    main()