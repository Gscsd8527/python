def funX(f):
    print('-----------开始------------')
    def funY():
        f()
        print('函数内。。。。')
    print('-----------结束-------------')
    return funY

# 装饰器
@funX#语法糖
def test():
    print('test......')

test()