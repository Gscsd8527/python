# 时间函数举例1
if __name__=='__main__':
    import time
    # 起始时间
    start=time.clock()
    for i in range(10000):
        print(i,end='')
    # 结束时间
    end=time.clock()
    print()
    print('different is %6.3f'%(end-start))