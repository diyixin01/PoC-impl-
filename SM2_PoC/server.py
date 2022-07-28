import sm3
import json
import socket


HOST = ''
PORT = 8050
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind((HOST, PORT))

print("客户端链接成功")
d = 9
n = 67
k,addr = client.recvfrom(1024)
k = int(k.decode(),16)
v,addr = client.recvfrom(1024)
v = int(v.decode(),16)

table = []
for i in range(20000 ,20000 + pow(2,16)):
    h = sm3._hash(str(i) + str(i))
    table.append(h)   
Q = []
for m in table:
    if m[:2] == k:
        Q.append((pow(int(m,16),d))%n)

print("Q:",Q)

# 计算H_ab
H_ab=(pow(v,d))%n


client.sendto(hex(H_ab).encode(),addr)
json_v = json.dumps(V)
client.sendto(json_v.encode('utf-8'),addr)
client.close()

print("服务器端关闭")
