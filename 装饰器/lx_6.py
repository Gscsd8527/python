# 底锅，羊肉
# 麻酱、豆皮
# 麻酱、香菜
lst=[]
def f_a1(f):
    def f_b1():
        f()
        c=5
        lst.append(c)
        print('1.麻酱、香菜的价格为：%d'% c)
    return f_b1
def t_a1(f):
    def t_b1():
        f()
        b=10
        lst.append(b)
        print('2.麻酱、豆皮的价格为：%d'% b)
    return t_b1
@f_a1
@t_a1
def my_test():
    a=40
    lst.append(a)
    print('底锅：底锅 羊肉价格为：%d'% a)
my_test()
sun=0
for i in lst:
    sun+=i
print('花了%d元钱吃的火锅'% sun)

