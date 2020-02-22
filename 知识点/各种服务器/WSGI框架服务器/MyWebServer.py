from socket import *
from multiprocessing import Process
import re
import sys

class HTTPServer(object):
    """"""
    def __init__(self, app_temp):
        """构造函数"""
        self.sSocket = socket(AF_INET, SOCK_STREAM)
        self.sSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.app = app_temp
        
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
        print("get request:\r\n" + str(request_lines))
        request_first_line = request_lines[0]
        # 正则表达式提取用户请求的文件名：/index.html
        request_file = re.match(r"\w+ +(/[^ ]*) ",request_first_line).group(1)
        method = re.match(r"(\w)+ +/[^ ]* ",request_first_line).group(1)

        environ={ 
            "PATH_INFO":request_file,
            "METHOD": method
            }
        response_body = self.app(environ, self.start_response)
        #结合相应头与响应体成为完整的HTTP相应信息
        response_data = self.response_headers + "\r\n" + response_body

        # 向用户发送相应报文,无论是脚本还是静态文件。
        cSocket.send(response_data.encode())
        cSocket.close()

def main():
    # sys.path.insert(1,WSGI_PYTHON_DIR)
    # 理想启动命令 python3 MyWebServer.py MyWebFramWork:app
    if len(sys.argv) < 2:
        sys.exit("-----------------\ninput @ shell:\ncd /Users/zhanengeng/Documents/GitHub/mysite/知识点/各种服务器/WSGI框架服务器\npython3 MyWebServer.py MyWebFramwork:app")
    module_name, app_name = sys.argv[1].split(":") 
    #module_name == "MyWebFramWork.py"; app_name == "app"
    m = __import__(module_name)
    app = getattr(m, app_name)  #getattr(对象, "属性1") 从对象里取属性
    http_server = HTTPServer(app)
    http_server.bind(8080)
    http_server.start()

if __name__ == "__main__":
    main()
