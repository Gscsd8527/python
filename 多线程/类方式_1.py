# 类方法单线程
import _thread
import threading
import time
class mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        print('mythread')
    def run(self):
        for i in range(11):
            print(i)
            time.sleep(1)
t=mythread()
t.start()
# 线程名字
# t.getName()
# print(t)
# 继承了父类的start方法，会自动调用run()方法，可以重写，但会失去其中的意义
a=threading.active_count()
b=threading.current_thread()
print(b)
print(a)
# c=threading.enumerate()
# print(c)

