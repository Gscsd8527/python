# 3.序列化，反序列化（定义一个类，生成对象）
import pickle
class test:
    def __init__(self,name):
        self.name=name
    def tst(self):
        print('{}超级无敌大帅哥'.format(self.name))
tan=test('谭振华')
tt=tan.tst()

output=open('G:/pythonfile/zy1.txt','wb')
pickle.dump(tt,output)
output.close()
x=output=open('G:/pythonfile/zy1.txt','rb')
pickle.load(output)
print(x)
output.close()