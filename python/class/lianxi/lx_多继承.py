class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def fac_a(self):
        print('%d,%d-----------A'%(self.a,self.b))
class B:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def fac_b(self):
        print('%d,%d-----------B'%(self.a, self.b))
class C(A,B):
    def __init__(self,a,b,c,d,e,f):
        A.__init__(self,a,b)
        B.__init__(self,a,b)
        self.a=a
        self.b=b
    def fac_c(self):
        print('%d,%d-----------C'%(self.a, self.b))
c=C(1,2,3,4,5,6)
c.fac_c()
c.fac_a()