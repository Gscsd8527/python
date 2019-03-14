# 如何使用join方法
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
for j in range(30,19,-1):
    print(j)
    # 先把t执行完后再执行j
    t.join()
    time.sleep(1)
