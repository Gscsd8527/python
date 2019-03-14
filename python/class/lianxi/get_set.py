class tan:
    def __init__(self,age):
        self.age=age
    def __set__(self,uage):
        if self.age<0:
            self.age=uage
    def __get__(self):
        return self.age
t=tan(-2)
t.__set__(20)
print(t.age)