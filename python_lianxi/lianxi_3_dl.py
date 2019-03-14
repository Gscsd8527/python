User='tan'
name='123456'
while 1:
    print('-------------------------------------------------------')
    print('欢迎进入学院管理系统V1.0')
    print('1. 登录')
    print('2. 退出')
    print('3. 认证')
    print('4. 修改密码')
    print('-------------------------------------------------------')
    dl = int(input("输入您的选择："))
    if dl ==1:
        user=input("请您输入您的用户名:")
        if user == User:
            Name =input('请您输入您的密码：')
            if Name==name:
                print("欢迎您登录")
            else:
                print('密码错误，请您重新输入：')
                Name = input('请您输入您的密码：')
                if Name==name:
                   print("欢迎您登录")
                else:
                    print('输入错误')
    elif dl==2:
        print('退出')
    elif dl==3:
        print('认证')
    elif dl==4:
        tag_name=input('请输入您的原始密码：')
        if tag_name==name:
            name=input('请输入新的密码: ')
    else:
        print('输入错误')

