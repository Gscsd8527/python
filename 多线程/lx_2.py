# 查看当前时间
import time
lst = []
while 1:
    # 读取当前时间、日期、年份、星期几
    mytime=time.ctime(time.time())
    print(mytime)
    print(type(mytime))
    tp=mytime.replace('17','10086')
    # lst=tp.split()
    # print(lst)
    time.sleep(5)
    break
