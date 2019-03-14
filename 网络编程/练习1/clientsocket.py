import socket
import threading

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',9999))
print('客户端已连接')

def myrecv(c):
    while True:
        msg=c.recv(1024)
        print(msg.decode())
threading._start_new_thread(myrecv,(client,))

def myinput():
    while True:
        msg=input()
        client.send(msg.encode())
threading._start_new_thread(myinput())
