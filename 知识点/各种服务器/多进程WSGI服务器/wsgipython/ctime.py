import time 
def application(env, start_response):
    """固定格式"""
    status = "200 OK"
    headers =[
        ("Content-Type","text/plain")
    ]
    start_response(status, headers)

    """实际要返回内容"""
    return time.ctime()

