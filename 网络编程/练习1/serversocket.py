import socket
import threading

# 服务器端
#                          网络编程         以TCP（面向连接）方式连接
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定主机和端口，服务器写的是自己的IP地址
serversocket.bind(('127.0.0.1',9999))
# 最多监听5个
print('服务器已等待')
serversocket.listen(5)
# 等待客户端连接
print('最多同时连接5个客户')
# 接收客户端连接，c是元组，表示得到客户端的地址和端口
c=serversocket.accept()
print(c)
def myrecv(c):
    while True:
        msg=c[0].recv(1024) #接收消息
        print(msg.decode())
# 有参数时参数写在元组里面，函数不带括号
threading._start_new_thread(myrecv,(c,))

def myinput():
    while True:
        msg=input()
        c[0].send(msg.encode())
# 无参数时，函数要带括号
threading._start_new_thread(myinput())