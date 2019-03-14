# 类方法单线程
import _thread
import threading
import time
class mythread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name
        print('mythread')
    def run(self):
        for i in range(11):
            print('%s\t%d'%(self.name,i))
            time.sleep(1)
M1=mythread('mythread_1')
M2=mythread('mythread_2')
# 线程名字
# t=M1.getName()
# print(t)
# 继承了父类的start方法，会自动调用run()方法，可以重写，但会失去其中的意义
M1.start()
M2.start()
for j in range(50,39,-1):
    print(j)
    time.sleep(1)
a=threading.active_count()
b=threading.current_thread()
print(b)
print(a)
# c=threading.enumerate()
# print(c)

