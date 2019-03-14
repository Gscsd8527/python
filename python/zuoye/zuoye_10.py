# =======通讯录管理系统=======
# 1.增加姓名和手机
# 2.删除姓名
# 3.修改手机
# 4.查询所有用户
# 5.根据v姓名查找手机号
# 6.退出
# ============================
dct = {}
while 1:
    print('=======通讯录管理系统=======')
    print('1.增加姓名和手机')
    print('2.删除姓名')
    print('3.修改手机')
    print('4.查询所有用户')
    print('5.根据v姓名查找手机号')
    print('6.退出')
    my_cx=input('输入您要操作的序号：')
    if my_cx=='1':
        name=input('输入用户姓名：')
        while 1:
          tel=input('输入用户号码：')
          if len(tel)==11 and tel.isdigit():
             dct[name]=tel
             break
          else:
             print('手机号错误，请重新输入')
    elif my_cx=='2':
        while 1:
           name_tep=input('输入要删除的姓名：')
           if name_tep in dct.keys():
               del dct[name_tep]
               break
           else:
               print('要删除的姓名不存在')
    elif my_cx=='3':
        name_tp = input('输入要修改手机号的用户姓名：')
        while 1:
            tel_new=input('输入新的号码：')
            if len(tel_new)==11 and tel_new.isdigit():
                dct[name_tp]=tel_new
                break
            else:
                print('手机号输入错误')
    elif my_cx=='4':
        for ky in dct.keys():
            print(ky,dct[ky])
    elif my_cx=='5':
        while 1:
            name_te = input('输入要查询的姓名：')
            if name_te in dct.keys():
               print(dct[name_te])
               break
            else:
               print('该姓名不存在，请重新输入')
    elif my_cx=='6':
        print('退出')
    else:
        print('输入错误，请重新输入！')




