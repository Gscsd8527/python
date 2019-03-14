# 羊肉
def mutton(add):
    # print('您要加的是羊肉')
    def mu_money():
        print('一份羊肉的价格为15元')
        mu_part=int(input('您需要几份羊肉：'))
        print('您选择了{0}份羊肉，共计{1}元'.format(mu_part,mu_part*15))
        return 15*mu_part+add()
    return mu_money

# 蔬菜
def vaget(add):
    # print('您要加的是蔬菜')
    def vaget_money():
        print('蔬菜一份为5元')
        vaget_part=int(input('您需要几份蔬菜：'))
        print('您选择了{0}蔬菜，共计{1}元'.format(vaget_part, vaget_part * 5))
        return 5*vaget_part+add()
    return vaget_money

# 牛肉
def beef(add):
    # print('您要加的是牛肉')
    def beef_money():
        print('牛肉一份为40元')
        beef_part=int(input('您需要几份牛肉：'))
        print('您选择了{0}份牛肉，共计{1}元'.format(beef_part, beef_part * 40))
        return 40*beef_part+add()
    return beef_money

@mutton
@vaget
@beef
def huoguo():
    while True:
        print('1.清汤锅底  2.麻辣锅底  3.鸳鸯锅底')
        myinp = int(input('请选择你要的锅底：'))
        if myinp==1:
            print('清汤锅底20元')
            return 20
        elif myinp==2:
            print('麻辣锅底40元')
            return 40
        elif myinp==3:
            print('鸳鸯锅底30元')
            return 30
        else:
            print('输入错误，请重新输入！')
sum_money=huoguo()
print('总共需要支付：%d元'%sum_money)




