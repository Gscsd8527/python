class test:
    # 类属性
    uname='谭振华'
    def __init__(self,name):
        # 这里不再是对象属性，而是类属性，self改成了test
        test.uname=name
    def cuse(self):
        print('%s'%self.uname)
   # 类方法前面要加这个，而且函数里面参数不再是self，而是其他，可写为cls
    @classmethod
    def cmethod(cls):
        cls.uname='万古至尊'
        print('这是一个类方法')

    @staticmethod
    def smethod():
        # 用处;当有些东西写在一个类里面不合适时就可以写在静态方法内，
        # 无需参数，也不依靠类，可通过类和对象调用
        print('这是一个静态方法')
# 这里可以直接输，不用新建对象也可以，因为他是类属性和对象
test.cmethod()
print(test.uname)

t=test('李云霄')
t.cmethod()
# 这里不是类属性，而是对象里面重新开辟出来的对象属性
# t.uname='古飞扬'
t.cuse()
tt=test('古飞扬')
print(test.uname)
t.cuse()
