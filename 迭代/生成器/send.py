# send()方法：
#      1.send方法有一个参数，指定的是上一次挂起的yield语句的返回值
#      2.相比于.__next__() 可以额外的给yield语句传值
#      3.注意第一次调用 t.send(None)
def test():
    tep1=yield 1
    print('xxxxxxxxx')#只运行一个next,则这句不会执行
    print(tep1)

    tep2=yield 2
    print(tep2)

g=test()
print(g.__next__())
print(g.send('我最帅'))#如果上面没有那句输出，则报错，因为send只是挂起上一次的值
# 注销上面一句的话则报错，如果一定要注销的话，那么send里面放None