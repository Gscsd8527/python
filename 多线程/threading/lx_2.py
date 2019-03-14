import threading
import time
def work1():
    for i in range(10):
        time.sleep(0.1)
        print("-------------", i)

def work2():
    for i in range(10, 20):
        print("-------------", i)


start_time = time.time()
thread1 = [threading.Thread(target=work1, args=()) for i in range(20)]
# thread2 = threading.Thread(target=work2, args=())
for thread in thread1:
    thread.start()
for thread in thread1:
    thread.join()
end_time = time.time() - start_time
print('共花费 {} '.format(end_time))
# 共花费 1.0119073390960693
# thread1.start()
# thread2.start()

# start_time = time.time()
# for i in range(20):
#     work1()
# end_time = time.time() - start_time
# print('共花费 {} '.format(end_time))
# 共花费 20.11350107192993