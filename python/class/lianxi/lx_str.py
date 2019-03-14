class car:
    def __init__(self,name,rbj):
        self.name=name
        self.rbj=rbj

  # __str__用于输出一串字符串，在外部新建一个对象时并输出对象时，
  # 不写__str__则会输出一串地址，而写了则输出里面return里面返回的东西
    def __str__(self):
        return '%s的颜色是%s色'%(self.name,self.rbj)
kc=car('奔驰','银')
print(kc)