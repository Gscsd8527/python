# 定义一个列表，通过下标访问最后一个元素；list(list.length)
# 定义一个调用的方法：捕获异常
def test():
    lst = [1, 2, 3, 4, 5]
    n=lst[len(lst)]
    print(n)
def test2():
    try:
        test()
    except IndexError as t:
        print('下标超出')
        print(t)
test2()
