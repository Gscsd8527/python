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
for i in g:
    print(i)
print('-'*30)
# 下面这句不会执行，生成器只执行一次，如果再想执行的话，在创建一个就好了，g=test()，这里要重新再调用这个函数
for a in g:
    print(a)