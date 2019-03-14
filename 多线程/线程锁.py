import _thread
import threading
import time
class mythread(threading.Thread):
    def run(self):
        for i in range(1,11):
            # 关锁
            cond.acquire()
            print(i)
            # 开锁
            cond.release()
lock=threading.Lock()
cond=threading.Condition(lock=lock)
M1=mythread()
M2=mythread()
M1.start()
M2.start()
# 等待多长时间
# cond.wait(1)
# 通知等待的锁要启动了
# 作用：当前线程哪个在等待，通知该线程马上要启动了
# cond.notify()
# 让等待的所有线程全部启动
# cond.notify_all()


