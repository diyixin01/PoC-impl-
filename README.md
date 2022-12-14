# PoC-impl


# 项目介绍

使用socket编程，实现账号密码的检查

# 运行指导

首先找到我们代码的地址，进行复制C:\Users\legion\Desktop\1，然后打开命令行窗口输入cd进入文件夹


![image](https://user-images.githubusercontent.com/75195549/181517389-c15756b2-7932-4fa4-8d3b-6944c6014700.png)



随后输入py server.py运行程序：

![image](https://user-images.githubusercontent.com/75195549/181517516-71a86a7e-e426-41b0-930d-ca9f367dd206.png)


记住：先运行服务器端再运行客户端



# socket编程介绍


计算机网络通信中各种协议相当复杂，例如三次握手，累计确定，分组缓存，但是这些应该属于操作系统内核的部分，但是对于应用程序来讲，操作系统需要抽象出一个概念，让上层应用去编程，这个概念就是socket。

socket就像插座一样，客户端的插头插进服务器插座，就建立了连接

这个socket可以理解成（客户端ip，客户端port，服务器ip，服务器端port），ip用来区分不同主机，port端口用来区分主机中不同的进程。
socket是“open—write/read—close”模式的一种实现，那么socket就提供了这些操作对应的函数接口。



# 服务器伪代码
```
listenfd=socket（.....）；
bind（listenfd，本机的ip和知名端口，....）;
listen（listenfd，....）；
while（true）
{
    connfd=accept（listenfd，....）；
    receive（connfd，....）；//这里读取客户端send的数据
    send（connfd，....）；
}
```


# 客户端伪代码

```
clienfd=socekt（.....）;
connect（clienfd，服务器的ip和port，.....）；
send（cliend，数据）； //这里的发送就相当于上面的read（）
receive（clienfd，....）；
close（clienfd）
```


# 实验原理

第一步：服务器生成数据


![image](https://user-images.githubusercontent.com/75195549/181519727-b188c7aa-6d40-4a76-a862-cbaa92dc445a.png)


第二步：客户端生成数据并发送给服务器



![image](https://user-images.githubusercontent.com/75195549/181519985-d176bd9e-58aa-47bf-a6d1-ed8a8ff5d3f1.png)


第三步：找寻数据组




![image](https://user-images.githubusercontent.com/75195549/181520052-d28d5f46-7b85-4346-a347-7a8fadd93856.png)


第四步：验证



![image](https://user-images.githubusercontent.com/75195549/181520118-f7eb0362-c3a3-4fef-a0fe-66b66c5ed279.png)




# 代码分析

# server.py
## Data receive

![image](https://user-images.githubusercontent.com/75195549/181522008-6cd28c11-1e89-477a-8573-ecdd2c772e92.png)


## create k-value table


![image](https://user-images.githubusercontent.com/75195549/181522138-2296e947-4a33-49e5-a9d2-0a5248b8abeb.png)



## compute h^ab

![image](https://user-images.githubusercontent.com/75195549/181522268-c36fc2a0-43cf-41b1-97a2-64c86ab60cea.png)


## send H_ab and data set

![image](https://user-images.githubusercontent.com/75195549/181522379-16da104e-331d-47a9-a752-97961c3f777b.png)


# client.py
## compute key-value

![image](https://user-images.githubusercontent.com/75195549/181522567-a254ded1-cc62-49a2-bf00-984fef899c7b.png)



## send k and v



![image](https://user-images.githubusercontent.com/75195549/181522688-e0e1b70f-5cd3-48a3-acfa-0e5c6f6c38fc.png)


## receive H_ab and data set S


![image](https://user-images.githubusercontent.com/75195549/181522786-2b385fa8-2980-4177-9bb5-f241a9b525a0.png)



## detection


![image](https://user-images.githubusercontent.com/75195549/181522846-aebd8474-3d62-42a8-b14c-33e87207d9c4.png)






# 结果展示


![image](https://user-images.githubusercontent.com/75195549/181516557-bc8f58c1-98c0-4333-91d1-36e423374108.png)


