class pet:
    def __init__(self,name):
        self.name=name
    def show(self):
        print('{0}动物在叫。。。'.format(self.name))
class yiyuan:
    def cure(self,pet):  #这里这个pet随便取的变量，和pet类没关系
        print('{}在治病'.format(pet.name))
        pet.show()
class dog(pet):
    def show(self):
        print('{0}汪汪叫。。。'.format(self.name))
class cat(pet):
    def show(self):
        print('{0}喵喵叫。。。'.format(self.name))
mydog=dog('二哈')
mydog.show()
mycat=cat('橘猫')
mycat.show()
yy=yiyuan()
yy.cure(mydog)
yy.cure(mycat)