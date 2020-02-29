"""适用于服务器和脚本为同一人编写的情况"""

from socket import *
from multiprocessing import Process
import re
import sys

# 设置静态文件根目录（常量，用大写。）
HTML_ROOT_DIR =  "/Users/zhanengeng/Documents/GitHub/mysite/知识点/各种服务器/多进程服务器/html"
WSGI_PYTHON_DIR ="/Users/zhanengeng/Documents/GitHub/mysite/知识点/各种服务器/多进程服务器/wsgipython"

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

    def start_response(self, status, script_headers):
        #WSGI传参
        server_headers = [
            ("Server","My Server")
        ]

        # 拼接响应头
        response_headers = "HTTP/1.1" + status + "\r\n"
        for headers in server_headers + script_headers:
            response_headers += f"{headers[0]}: {headers[1]}\r\n"
        # 把拼接好的响应头设为实例属性，以便其他方法直接调用。为什么不用return：因为脚本调用此方法时，不需要也不会接受返回值。脚本只负责传参。
        self.response_headers = response_headers 

    def handle_socket(self, cSocket, cAddr):
        """处理客户端请求"""
        request_data = cSocket.recv(1024).decode()

        # 逐行拆开报文
        request_lines = request_data.splitlines()
        print("TEST:\r\n" + str(request_lines))
        request_first_line = request_lines[0]
        # 正则表达式提取用户请求的文件名：/index.html
        request_file = re.match(r"\w+ +(/[^ ]*) ",request_first_line).group(1)

        if request_file.endswith(".py"): #假如是脚本
            try:
                module = __import__(request_file[1:-3]) #等于import ** as module。去掉/和.py。
            except Exception:
                self.response_headers = "HTTP/1.1 404\r\n"
                response_body = "Not Found"
            else:
                environ={ 
                    "PATH_INFO":request_file
                    }
                response_body = module.application(environ, self.start_response)
                #结合相应头与响应体成为完整的HTTP相应信息
            response_data = self.response_headers + "\r\n" + response_body

        else:
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
                response_start_line = "HTTP/1.1 404\r\n"
                response_headers = "Server: My server\r\n"
                response_body = "The file is note found!"

            else:
                # 创建相应头&相应体
                response_start_line = "HTTP/1.1 200\r\n"
                response_headers = "Server: My server\r\n"
                response_body = file_data

            finally:
                # 制作HTTP规范的相应报文，注意头/体间有空行
                response_data = response_start_line + response_headers + "\r\n" + response_body

        # 向用户发送相应报文,无论是脚本还是静态文件。
        cSocket.send(response_data.encode())
        cSocket.close()

def main():
    sys.path.insert(1,WSGI_PYTHON_DIR)  #把脚本存放文件夹添加到模块搜索路径。
    http_server = HTTPServer()
    http_server.bind(8080)
    http_server.start()

if __name__ == "__main__":
    main()
