def funX(f):
    print('-----------开始111111------------')
    def funY():
        f()
        print('函数内111111。。。。')
    print('-----------结束111111-------------')
    return funY

def fx(f):
    print('-----------开始222222------------')
    def fy():
        f()
        print('函数内222222。。。。')
    print('-----------结束222222-------------')
    return fy

@funX
@fx
def test():
    print('test......')

text=test()
test
