class student:
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age
    def my_set(self,new_age):
        if self.age<0:
            print('年龄错误')
            self.age = new_age
    def my_get(self):
        return self.age
tan=student('tanzhenhua','nan',-2)
tan.my_set(22)
tan.my_get()
print(tan.age)


