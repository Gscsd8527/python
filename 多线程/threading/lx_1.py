import threading
import time
def work():
    print('test')
    time.sleep(1)
if __name__ == '__main__':
    # start_time = time.time()
    # for i in range(10):
    #     work()
    # end_time = time.time()-start_time
    # print('共花费 {} '.format(end_time))
# 共花费 10.05716609954834
    start_time = time.time()
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=work))
    for thread in threads:
        thread.start()
    # for thread in threads:
    #     thread.join()
    end_time = time.time() - start_time
    print('共花费 {} '.format(end_time))
# 共花费 0.003001689910888672

