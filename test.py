import requests

from pycurl_client import Request, RequestAsync, RequestThread

http = Request()

http.set_option()  # 新增配置项
http.impersonate()  # 修改tls指纹
http.set_proxy('http://127.0.0.1:8888')  # 添加代理
http.set_cookie_file()  # 设置cookie的文件
res = http.get('https://www.baidu.com')
print(res.content.decode())
print(res.http_code)
