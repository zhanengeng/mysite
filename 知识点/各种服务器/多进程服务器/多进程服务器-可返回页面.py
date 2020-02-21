from socket import *
from multiprocessing import Process
import re

# 设置静态文件根目录（常量，用大写。）
HTML_ROOT_DIR =  "/Users/zhanengeng/Documents/GitHub/mysite/知识点/各种服务器/多进程服务器/html"

class HTTPServer(object):
    """"""
    def __init__(self):
        self.sSocket = socket(AF_INET, SOCK_STREAM)
        self.sSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        
    def bind(self,port):
        self.sSocket.bind(("",port))

    def start(self):
        self.sSocket.listen(128)  #行为，开始监听
        while True:
            cSocket, cAddr = self.sSocket.accept()
            p = Process(target=self.handle_socket, args=(cSocket, cAddr))
            #监利线程，把客户端扔进去
            p.start()
            cSocket.close()#记得在主进程里关闭客户端socket。

    def handle_socket(self, cSocket, cAddr):
        """处理客户端请求"""
        request_data = cSocket.recv(1024).decode()

        # 逐行拆开报文
        request_lines = request_data.splitlines()
        print("TEST:\r\n" + str(request_lines))
        request_first_line = request_lines[0]
        # 正则表达式提取用户请求的文件名：/index.html
        request_file = re.match(r"\w+ +(/[^ ]*) ",request_first_line).group(1)

        # 附加功能，把主页设为index.html 
        if "/" == request_file:
            request_file = "/index.html"

        #合并根目录与文件名
        file_name = HTML_ROOT_DIR + request_file

        # 提取内容
        try:
            with open(file_name, "r") as f:
                file_data = f.read()

        except IOError:
            response_header = "http1.1 404 OK\r\nServer: My server\r\n" 
            response_body = "NO SUCH PAGE!"

        else:
            # 创建相应头&相应体
            response_header = "http1.1 200 OK\r\nServer: My server\r\n" 
            response_body = file_data

        finally:
            # 制作HTTP规范的相应报文，注意头/体间有空行
            response_data = response_header + "\r\n" + response_body
            # 向用户发送相应报文
            cSocket.send(response_data.encode())
            cSocket.close()

def main():
    http_server = HTTPServer()
    http_server.bind(8080)
    http_server.start()

if __name__ == "__main__":
    main()
