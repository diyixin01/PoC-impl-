# PoC-impl


# 项目介绍

使用socket编程，实现账号密码的检查

# 运行指导

首先找到我们代码的地址，进行复制C:\Users\legion\Desktop\1，然后打开命令行窗口输入cd进入文件夹


![image](https://user-images.githubusercontent.com/75195549/181517389-c15756b2-7932-4fa4-8d3b-6944c6014700.png)



随后输入py SM2_PoC_server.py运行程序：

![image](https://user-images.githubusercontent.com/75195549/181517516-71a86a7e-e426-41b0-930d-ca9f367dd206.png)


记住：先运行服务器端再运行客户端



# socket编程介绍


    计算机网络通信中各种协议相当复杂，例如三次握手，累计确定，分组缓存，但是这些应该属于操作系统内核的部分，但是对于应用程序来讲，操作系统需要抽象出一个概念，让上层应用去编程，这个概念就是socket。


   socket就像插座一样，客户端的插头插进服务器插座，就建立了连接


   这个socket可以理解成（客户端ip，客户端port，服务器ip，服务器端port），ip用来区分不同主机，port端口用来区分主机中不同的进程。
socket是“open—write/read—close”模式的一种实现，那么socket就提供了这些操作对应的函数接口。



#服务器端伪代码

''listenfd=socket（.....）；
bind（listenfd，本机的ip和知名端口，....）;
listen（listenfd，....）；
while（true）
{
    connfd=accept（listenfd，....）；
    receive（connfd，....）；//这里读取客户端send的数据
    send（connfd，....）；
}
''








# 结果展示


![image](https://user-images.githubusercontent.com/75195549/181516557-bc8f58c1-98c0-4333-91d1-36e423374108.png)


