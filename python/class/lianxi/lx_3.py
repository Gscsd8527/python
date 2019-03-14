class car:
    def __init__(self,name):
        self.name=name
    def xs(self):
        print('%s行驶了100公里'%self.name)
class kache(car):
    def __init__(self,name,zaizhong,fangfa):
        car.__init__(self,name)
        # 这里也可这样写
        # car.name=name
        self.zaizhong=zaizhong
        self.fangfa=fangfa
    def xs(self):
        print('{0}载重了{1}吨，行驶了{2}公里'.format(self.name,self.zaizhong,self.fangfa))
class huoche(car):
    def __init__(self,name,geshu,fangfa):
        car.__init__(self,name)
        self.geshu=geshu
        self.fangfa=fangfa
    def xs(self):
        # 在子类中调用父类的方法
        super().xs()
        print('{0}共有{1}节车厢，行驶了{2}公里'.format(self.name,self.geshu,self.fangfa))
kc=kache('卡车',100,108)
kc.xs()
hc=huoche('火车',36,108)
hc.xs()



