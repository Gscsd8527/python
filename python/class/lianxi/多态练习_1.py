class bird:
    def __init__(self,name):
        self.name=name
    def jiao(self):
        print('渣渣叫')
    def aggress(self):
        print('fff')
class bird_method:
    def agg1(self,bird):
        print('{}'.format(bird.name))
        print('弹射飞')
        bird.jiao()
        bird.aggress()
class split_bird(bird):
    def aggress(self):
        print('分裂攻击')
    def jiao(self):
        print('嗷嗷叫。。。')

class huojian_bird(bird):
    def aggress(self):
        print('加速冲撞')

class red_bird(bird):
    def aggress(self):
        print('普通攻击')

class bomb_bird(bird):
    def aggress(self):
        print('爆炸攻击攻击')

class fatty_bird(bird):
    def aggress(self):
        print('扔蛋攻击')
    def jiao(self):
        print('不叫')

splt=split_bird('分裂鸟')
b_method=bird_method()
b_method.agg1(splt)


b=bomb_bird('炸弹鸟')
a=bird_method()
a.agg1(b)

# bd=bird()
# bd.agg(bird)
# hj=huojian_bird('火箭鸟')
# red=red_bird('红色鸟')
# bomb=bomb_bird('炸弹鸟')
# fatty=fatty_bird('胖子')