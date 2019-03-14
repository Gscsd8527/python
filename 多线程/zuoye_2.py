# 我们经常在银行存钱、取款，其中一个线程负责存钱，另一个线程负责取款。
# 如果不加控制，很容易就把钱数算错了。我们看看银行是怎么算错钱数的：
import threading

# 变量money被t1和t2两个线程共享
money=0
# 存钱
def put_money(sum):
    global money
    money+=sum

# 取钱
def get_money(sum):
    global money
    money-=sum

def run_thread(sum):
    for i in range(100): #执行的次数要足够多
        # 先存sum,后取sum,钱数应当为0
        put_money(sum)
        get_money(sum)

t1=threading.Thread(target=run_thread, args=(100,))
t2=threading.Thread(target=run_thread,args=(1000,))
t1.start()
t2.start()
t1.join()
t2.join()
print(money)