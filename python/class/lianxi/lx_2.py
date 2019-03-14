# 学生类
# 属性：姓名 性别 身高 体重
# 方法：show() kaoshi()
class student:
    def __init__(self,name,sex,gao,tg,cj):
        self.name=name
        self.sex=sex
        self.gao=gao
        self.tg=tg
        self.cj=cj

    def show(self):
        print('我叫{0} 性别：{1} 身高：{2}，体重：{3}'.format(self.name,self.sex,self.gao,self.tg))
    def kaoshi(self):
        if self.cj>60:
            print('{0}考试{1}分，考试及格'.format(self.name, self.cj))
        else:
            print('{0}考试{1}分，考试不及格'.format(self.name, self.cj))
        # 也可以在参数内定义参数
    def new_default(self,new_default_canshu):
        print('gg%s----------%s'%(new_default_canshu,self.name))

# 新建对象就要赋值
tanzhenhua=student('谭振华','男','175','60kg',100)
tanzhenhua.show()
tanzhenhua.kaoshi()
tanzhenhua.new_default('dd')
dj=student('王深泉','男','160','70kg',0)
dj.show()
dj.kaoshi()
