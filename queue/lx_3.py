import queue
import threading
import time


class Consumer(threading.Thread):
    def __init__(self,que,lst):
        threading.Thread.__init__(self)
        self.que = que
        self.lst = lst
    def run(self):
        print('启动 Consumer')
        for i in self.lst:
            self.que.put(i)

class Producer(threading.Thread):
    def __init__(self,que):
        threading.Thread.__init__(self)
        self.que = que
    def run(self):
        while True:
            if self.que.empty():  #队列为空
                return
            else:
                a = self.que.get()  #从队列中取出数据
                if a is not None:
                    for b in range(a[0],a[1]):
                        print(b)
                    self.que.task_done()  # 告诉线程我完成了这个任务，是否继续join阻塞，让线程向前执行或者退出
                else:
                    pass

def test(lst):
    for i in lst:
        for m in range(i[0],i[1]):
            print(m)
if __name__ == '__main__':
    lst = [(1,20000),(3,40000),(5,60000)]
    start_time = time.time()
    q = queue.Queue(10)
    # 出队
    lt = Consumer(q,lst)
    # 入队
    data = Producer(q)
    # 启动线程
    lt.start()
    data.start()
    # 阻塞等待子线程执行完毕后再执行主线程
    lt.join()
    data.join()
    # test(lst)
    end_time = time.time()
    end_time = end_time - start_time
    print('共花费了{}'.format(end_time))

#不使用多线程的情况下，花费了0.015011....秒
#使用了多线程后花费了0.009.....秒