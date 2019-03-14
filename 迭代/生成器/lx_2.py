# 生成器的创建方式
#  yield 可以去阻断当前的函数取执行，然后，当使用next（）函数，或者__next__()，
# 都会让函数继续执行，然后，当执行到下一个yield语句的时候，又会被暂停
def test():
    print('xxxxxxxxxxxxx')
    yield 1
    print('a')

    yield 2
    print('b')

    yield 3
    print('c')

    yield 4
    print('d')
g=test()
print(g)
print(next(g))
print(next(g))