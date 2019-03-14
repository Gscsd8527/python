import socket
import threading

clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('127.0.0.1',9999))
print('客户端已连接')

def my_recv(adr):
    while True:
        mystr=adr.recv(1024)
        print(mystr.decode())
threading._start_new_thread(my_recv,(clientsocket,))

def my_send():
    while True:
        mystr=input()
        clientsocket.send(mystr.encode())
threading._start_new_thread(my_send())