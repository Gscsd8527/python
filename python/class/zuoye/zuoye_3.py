# .写一个递归函数,传入一个数字返回它的阶乘.
def test(x):
    sun = 1
    while x:
        sun*=x
        x-=1
    print('阶乘为：%d'%sun)
num=int(input('请输入你要求的阶乘数：'))
test(num)
