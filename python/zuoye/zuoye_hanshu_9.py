# 9、将通讯录管理系统改成函数的形式实现
# =======通讯录管理系统=======
# 1.增加姓名和手机
# 2.删除姓名
# 3.修改手机
# 4.查询所有用户
# 5.根据v姓名查找手机号
# 6.退出
# ============================
def add(mydct):
    name = input('输入用户姓名：')
    while 1:
        tel = input('输入用户号码：')
        if len(tel) == 11 and tel.isdigit():
            mydct[name] = tel
            break
        else:
            print('手机号错误，请重新输入')
def scxm(mydct):
    name_tep = input('输入要删除的姓名：')
    if name_tep in mydct.keys():
        del mydct[name_tep]
    else:
        print('要删除的姓名不存在')
def xg_tel(mydct):
    name_tp = input('输入要修改手机号的用户姓名：')
    while 1:
        tel_new = input('输入新的号码：')
        if len(tel_new) == 11 and tel_new.isdigit():
            dct[name_tp] = tel_new
            break
        else:
            print('手机号输入错误')
def cx(mydct):
    for ky in mydct.keys():
        print(ky, mydct[ky])
def xm_tel(mydct):
    while 1:
        name_te = input('输入要查询的姓名：')
        if name_te in mydct.keys():
            print(mydct[name_te])
            break
        else:
            print('该姓名不存在，请重新输入')
dct = {'tanzhenhua':14779569000}
while 1:
    print('=======通讯录管理系统=======')
    print('1.增加姓名和手机')
    print('2.删除姓名')
    print('3.修改手机')
    print('4.查询所有用户')
    print('5.根据v姓名查找手机号')
    print('6.退出')
    my_cx=int(input('输入您要操作的序号：'))
    if my_cx==1:
        add(dct)
    elif my_cx==2:
        scxm(dct)
    elif my_cx==3:
        xg_tel(dct)
    elif my_cx==4:
        cx(dct)
    elif my_cx==5:
        cx(dct)
    elif my_cx==6:
        print('退出')
        break
    else:
        print('输入错误，请重新输入')


