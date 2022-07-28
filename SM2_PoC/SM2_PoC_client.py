import sm3
import sys
import json
import socket






HOST = '127.0.0.1'
PORT = 8050
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



d = 5
n = 23
name = liujinyuan
password = 246319
try:
    client.connect((HOST, PORT))
    print("客户端链接成功")
except Exception:
    print('连接失败')
    sys.exit()
else:
    # 客户端计算key-value
    h = sm3._hash(str(name)+str(password))
    k = h[:2]
    v = str((pow(int(h,16),d))%n)


    addr = (HOST, PORT)
    client.sendto(k.encode('utf-8'), addr)
    client.sendto(v.encode('utf-8'), addr)

    # 从服务端接收H_ab与data set S
    H_ab,addr = client.recvfrom(1024 * 5)
    H_ab = int(H_ab.decode(),16)
    json_v,addr = client.recvfrom(1024 * 5)
    json_v = json_v.decode('utf-8')
    S = json.loads(json_v)
    print("Sig:",S)

    # 计算并检查H_b是否在S中
    H_b = (pow(H_ab,sm3.inv(d,n-1)))%n
    tmp = 0
    for item in S:
        b = item
        if b == H_b:
            tmp = 1
    if tmp == 0:
        print('账户',name,'安全')
    else:
        print('账户',name,'不通过')
