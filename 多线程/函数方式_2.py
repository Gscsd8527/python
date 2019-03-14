# 多线程
import _thread
import threading
import time
def test():
    for i in range(1,10):
        print(i)
        time.sleep(1)
print('------main-------')
# 启动线程
threading._start_new_thread(test,())
for i in range(50,39,-1):
    print(i)
    time.sleep(1)
# 不结束线程
input()

