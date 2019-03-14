# 底锅，羊肉
# 麻酱、豆皮
# 麻酱、香菜
def f_a1(f):
    def f_b1():
        f()
        print('麻酱、香菜')
        return 5+f()
    return f_b1
def t_a1(f):
    def t_b1():
        f()
        print('2.麻酱、豆皮')
        return 10+f()
    return t_b1
@f_a1
@t_a1
def my_test():
    print('底锅：底锅 羊肉')
    return 40
my_money=my_test()
print('花了%d元钱吃的火锅'% my_money)