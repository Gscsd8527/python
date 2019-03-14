class A:
    def f_a(self):
        print('--------A--------')
class B:
    def f_a(self):
        print('-------B-------')
class C(A,B):
    def f_a(self):
        super().f_a()
        # 1. 把对象调用转换成类调用，需要注意的是这时self参数需要显式传递
        # 缺点：
        # 比如说如果修改了父类名称，那么在子类中会涉及多处修改，另外，Python是允许多继承的语言，
        # 如上所示的方法在多继承时就需要重复写多次，显得累赘。为了解决这些问题，Python引入了super()机制
        B.f_a(self)
        # 2.使用super()机制：  引入super（）方法来调用B类中的f_a()方法
        # 这里super（）里面写A则调用B的f_a方法，写C则调用A的f_a方法
        super(A,self).f_a()
        print('--------C--------')
c=C()
c.f_a()