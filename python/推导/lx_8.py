# set推导
# seq={x**2 for x in [1,1,2]}
# print(seq)
class tan:
    def __init__(self ,name):
        self.name=name
        print('ddddd')
    def __new__(cls, *args, **kwargs):
        print('这是new方法')
        return object.__new__(cls)
    def __del__(self):
        print('这是del方法')
t=tan(1)
del t
