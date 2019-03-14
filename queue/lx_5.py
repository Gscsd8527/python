import queue
import threading
import time

class Consumer(threading.Thread):
    def __init__(self, que, num):
        threading.Thread.__init__(self)
        self.que = que
        self.num = num
    def run(self):
        for i in range(self.num):
            print('存入第{}个数据'.format(i))
            self.que.put(i)


class Parducer(threading.Thread):
    def __init__(self, que):
        threading.Thread.__init__(self)
        self.que = que
    def run(self):
        while True:
            if not self.que.empty():
                tmp = self.que.get()
                print('消费数据')
                time.sleep(1)
                print(tmp)
            else:
                print('消费完，跳出循环')
                break

if __name__ == '__main__':
    q = queue.Queue()
    a = 100
    con = Consumer(q ,a)
    par = Parducer(q)
    con.start()
    par.start()
    con.join()
    par.join()