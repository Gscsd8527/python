class A:
    def __str__(self):
        return 'add method'
#A.f=lambda self,x:x*2
a=A()
print(a)
A.f=lambda self,x:x*2
b=A()
print(b.f(100))