# 2.（1）创建一个叫做People的类：
# 属性：姓名、年龄、性别、身高
# 行为：说话、计算加法、改名
# 编写能为所有属性赋值的构造方法；
# （2）创建主类：
# 创建一个对象：名叫“张三”，性别“男”，年龄18岁，身高1.80；
# 让该对象调用成员方法：
# 说出“你好！”
# 计算23+45的值
# 将名字改为“李四”
class people:
    def __init__(self,name,age,sex,heigh):
        self.name=name
        self.age=age
        self.sex=sex
        self.heigh=heigh
    def speak(self):
        print('你好！')
    def Add(self,num1,num2):
        print(num1+num2)
    def __set__(self,uname):
        self.name=uname
    def __get__(self):
        return self.name
tan=people('张三','男',18,180)
tan.speak()
tan.Add(23,45)
tan.__set__('李四')
print(tan.name)