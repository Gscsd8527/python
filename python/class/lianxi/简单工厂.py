#简单工厂
class Hambuger:
    def show(self):
        print("这是汉堡...")
class chickenHambuger(Hambuger):
    def show(self):
        print("这是鸡腿汉堡...")
class fishHambuger(Hambuger):
    def show(self):
        print("这是麦香鱼汉堡...")
class factory:
    @classmethod
    def createHambegur(cls,hum):
        if hum=="chicken":
            return chickenHambuger()
        else:
            return fishHambuger()
c=factory.createHambegur("fish")
c.show()