class test:
    # 创建对象
    def __new__(cls, *args, **kwargs):
         print('这是new方法')
         return object.__new__(cls)
    def __init__(self):
         print('初始化方法')
    def __del__(self):
        print('对象销毁。。。')
t=test()