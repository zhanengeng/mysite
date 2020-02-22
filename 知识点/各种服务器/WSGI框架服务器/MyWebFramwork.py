"""自建一个框架,这个框架好像得服务器端来建。脚本端拿到框架后，往里添加脚本就行"""
import time 
# from MyWebServer import HTTPServer

HTML_ROOT_DIR = "/Users/zhanengeng/Documents/GitHub/mysite/知识点/各种服务器/多进程服务器/html"

class Application(object):
    """框架的核心部分，也就是框架的主题程序，框架是通用的"""
    def __init__(self, urls):
        # 设置路由信息
        self.urls = urls
    
    def __call__(self, env, start_response):   #让类能像函数一样被调用。
        path = env.get("PATH_INFO", "/")  #设置默认值为"/" 既主页。
        #/static/index.html
        if path.startswith("/static"):
            # print("------访问静态文件-------")
            # 要访问静态文件
            file_name = path[7:]

            try:
                with open(HTML_ROOT_DIR + file_name, "rb") as f:
                    file_data = f.read().decode()

            except IOError:
                # 如果未找到路由信息，404错误
                status = "404 Not Found"
                headers = []
                start_response(status, headers)
                return "not found"
            else:
                status = "200 OK"
                headers = []
                start_response(status, headers)
                return file_data

        for url, handler in self.urls:
            if path == url:
                return handler(env, start_response) #如果匹配到，则return跳出方法
                #此时假如 path == url == "ctime", 那么handler() == show_ctime()


def show_ctime(env, start_response):
    status = "200 OK"
    headers =[
        ("Content-Type","text/plain")
    ]
    start_response(status, headers)
    return time.ctime()

def say_hello(env, start_response):
    status = "200 OK"
    headers =[
        ("Content-Type","text/plain")
    ]
    start_response(status, headers)
    return "hello!"

urls = [
        ("/", say_hello),
        ("/ctime", show_ctime),
        ("/sayhello", say_hello)
    ]

app = Application(urls)

# if __name__ == "__main__":
#     urls = [
#         ("/", say_hello),
#         ("/ctime", show_ctime),
#         ("/sayhello", say_hello)
#     ]
#     """作为主启动程序，导入web端模块"""
#     app = Application(urls)
#     http_server = HTTPServer(app)
#     http_server.bind(8080)
#     http_server.start()

