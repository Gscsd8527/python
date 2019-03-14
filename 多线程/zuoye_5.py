# 时间函数举例2
if __name__=='__main__':
    import time
    # 返回当前的时间戳
    start=time.time()
    for i in range(3000):
        print(i)
    end=time.time()
    print(end-start)