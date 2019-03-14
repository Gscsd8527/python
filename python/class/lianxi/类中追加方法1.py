class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return ('my name is {0},age:{1}'.format(self.name,self.age))
a=A('tanzhenhua',22)
print(a)
# 用 类A 来增加方法的话，b 中找不到方法 f
# A.f=lambda self,x:x*2
# b=A.f(100)
# 用对象来增加方法
a.f=lambda x:x*2
print(a.f(100))