class person:
    # def __init__(self,name,sex,height):
    #     self.name=name
    #     self.sex=sex
    #     self.height=height
    def eat(self):
        print('正在吃饭。。。。')
class son_person(person):
    pass
tan=son_person()
tan.eat()