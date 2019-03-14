import socket
from time import ctime
host='127.0.0.1' #主机IP
port=6666 #要连接的端口，可随意设置，但要在0-65535之内，而且还要是闲置的端口
bufsize=1024  #接收信息的最大值
Addr=(host,port)
udp_serversocket=socket.socket(socket.AF_INET,socket.SHUT_RDWR) #这里是udp连接
udp_serversocket.bind(Addr) #绑定主机IP和端口号
while True:
    print('服务器准备就绪......')
    data,addr=udp_serversocket.recvfrom(bufsize) #等待客户端的连接，接收客户端的数据和IP,传过来的数据是一个元组
    udp_serversocket.sendto('[%s] %s' % (ctime(),data),addr)
    print('接收的数据%s'%addr)




