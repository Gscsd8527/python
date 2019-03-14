import threading
import queue
import time

class Mythread(threading.Thread):
    def __init__(self,fun):
        threading.Thread.__init__(self)
        self.fun = fun
    def run(self):
        self.fun()

def worker():
    global data
    while True:
        if not q.empty():
            a = q.get()
            parse(a[0], a[1])
            time.sleep(1)
            data.append(a)
        else:
            for i in data:
                q.put(i)
            data = []
    # while not q.empty():
    #     a = q.get()
    #     parse(a[0],a[1])
    #     time.sleep(1)
    #     data.append(a)
    #     if q.empty():
    #         for i in data:
    #             q.put(i)
    #         print(data)
    #         data = []




def parse(qd, zd):
    mystr = qd + zd
    print('=============',mystr)

def main():
    threads = []
    for i in LstAdd:
        q.put(i)
    for i in range(thendNum):
        thread = Mythread(worker)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    LstAdd = [
        ('abcde1','adfa1'),
        ('abcde2','adfa2'),
        ('abcde3','adfa3'),
        ('abcde4','adfa4'),
        ('abcde5','adfa5'),
        ('abcde6','adfa6'),
        ('abcde7','adfa7'),
        ('abcde8','adfa8'),
        ('abcde9','adfa9'),
              ]
    data = []
    q = queue.Queue()
    thendNum = 3
    main()