#单例
# 比如窗口类，只有一个窗口，不管点多少次都只有一个
class singleton:
    __indtance=None
    def __new__(cls):
        if cls.__indtance==None:
            cls.__indtance=object.__new__(cls)
            return  cls.__indtance
        else:
            return  cls.__indtance
s=singleton()
ss=singleton()
print(id(s))
print(id(ss))

