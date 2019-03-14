import socket
host='127.0.0.1'
port=6666
bufsize=1024
Addr=(host,bufsize)
udpclient=socket.socket(socket.AF_INET,socket.SHUT_RDWR)
while True:
    data=input('>')
    udpclient.sendto(data,Addr)
    data,Addr=udpclient.recvfrom(bufsize)
    print('输入的数据是%s'%data)