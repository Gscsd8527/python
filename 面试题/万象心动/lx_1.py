# 删除文件夹
# import os
# os.rmdir('G:/test')

# 正则提取src
# mystr = '<img src="https://p1.ssl.qhimg.com/t0151320b1d0fc50be8.png" />'
# import re
# my_str = re.search('src="(.*)"', mystr)
# print(my_str.group(1))

# 提取json
# mydict = {'aa': ['''{"k1":123, "k2": 345,"k3":"ares"}''', ]}  # 双引号才行
# import json
# my_str = mydict['aa'][0]
# print(my_str)
# print(type(my_str))
# my_json = json.loads(my_str)
# print(my_json)
# print(type(my_json))


# 多线程
import threading
import time
def work1(a):
    print('------%s---------' % a, time.ctime())
    time.sleep(5)
    print('------%s---------' % a, time.ctime())
    # for i in range(1, 13):
    #     print(i)

mylist = ['a', 'b', 'c', 'd', 'e', 'f']
def work2(a):
    print('==========%s===========' % a, time.ctime())
    time.sleep(3)
    print('==========%s===========' % a, time.ctime())
    # for i in mylist:
    #     print(i)
thread1 = threading.Thread(target=work1, args=(1, ))
thread2 = threading.Thread(target=work2, args=(2, ))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
