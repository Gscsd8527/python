import socket
import threading
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind(('127.0.0.1',9999))
serversocket.listen(5)
adr,por=serversocket.accept()
print('adr={0} por={1}'.format(adr,por))
def my_recv(adr):
    while True:
        mystr=adr.recv(1024)
        print(mystr.decode())
threading._start_new_thread(my_recv,(adr,))

def my_send():
    while True:
        mystr=input()
        adr.send(mystr.encode())
threading._start_new_thread(my_send())
