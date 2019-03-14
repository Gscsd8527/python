# notify和wait用法
import _thread
import threading
import time
class Thread1(threading.Thread):
    def run(self):
        for i in range(1,11):
            if i==3:
                cond.acquire()
                # 等待
                cond.wait()
                cond.release()
            print(i)
            time.sleep(1)
class Thread2(threading.Thread):
    def run(self):
        for i in range(30,19,-1):
            print(i)
            time.sleep(1)
        cond.acquire()
        cond.notify()
        cond.release()
lock=threading.Lock()
cond=threading.Condition(lock=lock)
t1=Thread1()
t2=Thread2()
t1.start()
t2.start()