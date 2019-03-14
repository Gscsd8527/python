import socket
import threading
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind(('127.0.0.1',9999))
print('服务器已等待')
serversocket.listen(5)
# 定义一个全局的变量，用来存储聊天信息，临时存储当前抢到线程的数据
msg=None
lock=threading.Lock()
mythread=threading.Condition(lock=lock)


def server_recv(c,a):
    global msg
    while True:
        mystr=c.recv(1024) #接收消息
        mythread.acquire()#线程同步
        msg=str(a)+mystr.decode()
        print(msg)
        mythread.notify_all()
        mythread.release()

def server_send(c,a):
    global msg
    while True:
        mythread.acquire()
        mythread.wait()
        mythread.release()
        c.send(msg.encode())
        print(msg)


while True:
    c,a=serversocket.accept()
    threading._start_new_thread(server_recv,(c,a))
    threading._start_new_thread(server_send,(c,a))
