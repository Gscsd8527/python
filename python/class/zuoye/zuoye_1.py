# 电脑，玩家
# 玩家出拳：1 剪刀  2 石头  3 布
# 1
# 电脑出拳：1 剪刀  2 石头  3 布
# 2
# 判断谁输谁赢：而且要记录下来第几局
# 是否继续？y
# 玩家出拳：1 剪刀  2 石头  3 布
# 1
# 电脑出拳：1 剪刀  2 石头  3 布
# 2
# ......
# 输出结果：天上不下雨 vs 曹操
# 天上不下雨 赢了 XX局
# 平了XX局
# 曹操赢了XX局
# 最后结果：XX赢了
class computer:
    def __init__(self,com_jieguo):
        self.c_jieguo=com_jieguo

class people:
    def __init__(self,p_jieguo):
        self.p_jieguo=p_jieguo

class tep:
    def __init__(self):
        self.cishu=0
    def jilv(self):
        self.cishu+=1
        print('这是第%d次',self.cishu)
class panduan:
    def __init__(self,com_tep,p_tep):
        self.com_tep=com_tep
        self.p_tep=p_tep
    def guize(self):
        print('1  表示剪刀')
        print('2  表示石头')
        print('3  表示布')
    def pd(self,com_t,p_t):
        if com_t==p_t:
            print('这把算平局')
        elif com_t==p_t+1 or com_t==p_t+2:
            print('这把人赢了')
        elif p_t==com_t+1 or p_t==com_t+2:
            print('这把电脑赢了')

my_tep=tep()
my_tep.jilv()
# 记录次数每次调用都自增1
com_dn=computer(1)
tan=people(2)
pand=panduan(com_dn.c_jieguo,tan.p_jieguo)
pand.guize()
pand.pd(com_dn.c_jieguo,tan.p_jieguo)


