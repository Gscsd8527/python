from multiprocessing import Pool
import time
import random
def work(name):
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    p = Pool(10)
    for i in range(5):
        p.apply_async(work, args=('i', ))
    p.close()
    p.join()
