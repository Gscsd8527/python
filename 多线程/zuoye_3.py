# 多线程间的资源竞争，并修复这个问题
from threading import Thread

some_var=0
class Increment(Thread):
    def run(self):
        global some_var
        read_value=some_var
        print('some_var in %s is %d'%(self.name,read_value))
        some_var=read_value+1
        print('some_var in %s after increment is %d'%(self.name,some_var))
    def use_increment_thread(self):
        threads=[]
        for i in range(50):
            t=Increment()
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        print('After 50 modifications, some_var should have become 50')
        print('After 50 modifications, some_var is %d' % (some_var,))