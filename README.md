# pycurl_demo
pycurl编译和模板





### Pycurl是python的用于请求的第三方库，支持http2，能修改ja3指纹，底层是C语言写的


### 编译流程
> 1.下载pycurl的编译包

> 2.因为pycurl底层是有c所写，需要用到visual studio 生成工具，下载链接

> 3.以2022版本为例，下载生成工具后打开"x64 Native Tools Command Prompt for VS 2022"命令行窗口

> 4.cd 到pycurl包中的 pycurl-REL_7_45_2 文件夹中(如果需要把pycurl编译在虚拟环境中，请先激活虚拟环境)，输入命令:
python setup.py install --curl-dir=D:\pycurl\pycurl\lib\libcurl --use-libcurl-dll --openssl-dir=D:\pycurl\pycurl\lib\openssl --with-openssl
其中路径稍作修改，替换为包中正确路径,即可编译。


> 5.如果在运行代码的时候导入pycurl报错，提示dll文件找不到，请把pycurl\lib\libcurl\bin文件夹中的libcurl.dll文件移到已经编译好的pycurl的egg文件中(pycurl-7.45.2-py3.10-win-amd64.egg中


### 使用
> pycurl支持异步,单步和线程，具体操作请看代码详情
> ![图片](https://ice.frostsky.com/2024/08/30/473b3493ff6ccf44a0842dec4abdcf5e.png)