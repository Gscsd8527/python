class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def fac_a(self):
        print('%d,%d-----------A'%(self.a,self.b))
class B(A):
    def __init__(self,a,b,c,d):
        A.__init__(self,a,b)
        self.c=c
        self.d=d
    def fac_b(self):
        print('%d,%d-----------B'%(self.c, self.d))
class C(B):
    def __init__(self,a,b,c,d,e,f):
        B.__init__(self,a,b,c,d)
        self.e=e
        self.f=f
    def fac_c(self):
        print('%d,%d-----------C'%(self.e, self.f))
c=C(1,2,3,4,5,6)
c.fac_c()
c.fac_a()
c.fac_b()