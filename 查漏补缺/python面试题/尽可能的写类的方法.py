class Array:
    __list=[]
    def __init__(self,a):
        self.a=a
        print('init')
    def __get__(self):
        return self.a
    def __set__(self,value):
        if self.a>0:
            self.a=value
    def __str__(self):
        print('str')
    def __del__(self):
        print('del')
    def __add__(self, other):
        return self.a+other
    # def __new__(cls):
    #     return 'new方法'
    def __len__(self):
        print('len')
        return len(self.__list)
    def __call__(self, *args):
        print('args=%d',args)
        return args
    def __delete__(self, instance):
        print('delete')
        return instance
    def __lt__(self, other):
        return True
    def __le__(self, other):
        return True
    def __eq__(self, other):
        return True
    def __ne__(self, other):
        return True
    def __gt__(self, other):
        return True
    def __ge__(self, other):
        return True
a=Array(10)
c=a.__add__(10)
print(c)
