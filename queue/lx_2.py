import threading
import queue
import time

class Producer(threading.Thread):
    def __init__(self, q):
        self.q = q
        super(Producer, self).__init__()
    def run(self):
        print('producer')
        time.sleep(1)
        self.q.put(3)

class Consumer(threading.Thread):
    def __init__(self, q):
        self.q = q
        super(Consumer, self).__init__()
    def run(self):
        while True:
            try:
                print('Start to get')
                item = self.q.get_nowait()
                print('Got the item:', item)
                print('Got time:', time.ctime())
                break
            except Exception as exc:
                print(exc)

st = time.ctime()
q = queue.Queue(3)
c = Consumer(q)
p = Producer(q)
p.start()
c.start()
c.join()
print('Task begin time:', st )