def test():
    print('-' * 10)
    a=yield 1
#这里的print(a)会被send替换掉，相当于把send里面的内容传给了a，在使用send时，要注意它后面还有没有yield，
# 没有的话就会报超出StopIteration，这个是因为超出了迭代器的范围
    print(a)


    print('='*10)
    b=yield 2
    print('*'*2)
    print(b)
    yield 3
tp=test()
print(tp.__next__())
print(tp.send('tan'))
print(tp.send('zhenhua'))