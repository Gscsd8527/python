import threading
import time
# 存放馒头
lst=[]
class Huofu(threading.Thread):
    def run(self):
        while True:
            # 哪个吃货抢到了锁
            condchihuo.acquire()
            if len(lst)==0:
                for i in range(1,11):
                    lst.append(i)
                    print('伙夫生产的第%d个馒头'% i)
                    time.sleep(1)
                # 吃货吃馒头的时候加锁
                # condchihuo.acquire()
                # 通知吃货们吃馒头
                condchihuo.notify_all()
            condchihuo.release()
class ChiHuo(threading.Thread):
    mantou=None
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name
    def run(self):
        while True:
            condchihuo.acquire()
            if len(lst)>0:
                mantou=lst.pop()
            else:
                # condhuofu.acquire()
                # condhuofu.notify()
                # condhuofu.release()
                condchihuo.wait()
            condchihuo.release()
            if mantou is not None:
                print('{0}正在吃第{1}个馒头'.format(self.name,mantou))

lock1=threading.Lock()
condhuofu=threading.Condition(lock=lock1)
lock2=threading.Lock()
condchihuo=threading.Condition(lock=lock2)
huofu=Huofu()
huofu.start()
eat1=ChiHuo('t1')
eat2=ChiHuo('t2')
eat3=ChiHuo('t3')
eat1.start()
eat2.start()
eat3.start()

