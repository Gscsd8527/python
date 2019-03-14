class people(object):
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
    def action(self):
        print('hello,大家好！我叫{0}，我是{1}的'.format(self.name,self.sex))

class tan(people):
    def __init__(self,name,sex,aihao,like):
    # 继承父类的方法有四种：
    #第一种
    #     people.__init__(self,name,sex)
    #     self.aihao=aihao
    #     self.like=like
    # ---------------------------
    #第二种
    #     people.name=name
    #     people.sex=sex
    #     self.aihao=aihao
    #     self.like=like
# -----------------------
    #第三种
        # self.name=name
        # self.sex=sex
        # self.aihao=aihao
        # self.like=like
    # ---------------------------
        #4.其实这个super也可以不要，和第三种没区别
        super().__init__(name,sex)
        self.aihao=aihao
        self.like=like
    def act(self):
        print('我爱好是{0}，我喜欢{1}'.format(self.aihao,self.like))
t=tan('谭振华','男','钓鱼抓鱼旅游','面朝大海，春暖花开')
t.action()
t.act()