# 声明一个列表来存放书籍
lst=[]
class DVD_append:
    def __init__(self,name):
        self.name=name
    def dvd_app(self):
        print('此处实现新增DVD')
        self.name = input('请输入DVD名称： ')
        if len(lst) < 9:
            lst.append(self.name)
            print('新增《%s》成功！' % self.name)
        else:
            print('新增《%s》失败！货架已满' % self.name)
        print('*'*20)

class DVD_examine:
    def __init__(self,sequence,state,name,loan_data,loan_time):
        self.sequence=sequence
        self.state=state
        self.name=name
        self.loan_data=loan_data
        self.loan_time=loan_time
    def dvd_ex(self):
        print('----> 查看DVD')
        print()
        print('序号    状态    名称        借出日期    借出次数')
        for i in range(1,len(lst)):
            print('{0}    可借    《{1}》        {2}    1'.format(i,lst[i-1],d_loan.loan_data))
class DVD_del:
    def __init__(self,name):
        self.name=name
    def dvd_del(self):
        print('----> 删除DVD')
        print()
        self.name=input('请输入DVD名称： ')
        if self.name in lst:
            del lst[lst.index(self.name)]
            print('删除《%s》成功！'%self.name)
            print('* '*20)
        else:
            print('没有找到匹配信息！')
            print('* '*20)
class DVD_loan:
    def __init__(self,name,loan_data):
        self.name=name
        self.loan_data=loan_data
    def dvd_loan(self):
        print('---> 借出DVD')
        print()
        self.name=input('请输入DVD名称： ')
        self.loan_data=int(input('请输入借出日期：'))
        if self.name in lst:
            print("借出成功")
            # lst.pop(self.name)
            del lst[lst.index(self.name)]
        else:
            print('《%s》以被借出！'%self.name)
class DVD_return:
    def __init__(self,name,return_data,money):
        self.name=name
        self.return_data=return_data
        self.money=money
    # def dvd_return(self):

class DVD_quit:
    pass

class DVD:
    def __init__(self,new_append,examine,D_del,loan,D_return,D_quit):
        self.new_append=new_append
        self.examine=examine
        self.D_del=D_del
        self.loan=loan
        self.D_return=D_return
        self.D_quit=D_quit
    def DVD_system(self):
        while 1:
            print('欢迎使用迷你DVD 管理器')
            print('-----------------------------------')
            print('1. 新增DVD')
            print('2. 查看DVD')
            print('3. 删除DVD')
            print('4. 借出DVD')
            print('5. 归还DVD')
            print('6. 退出DVD')
            print('-----------------------------------')
            my_inp=int(input('请选择; '))
            if my_inp==1:
                self.new_append.dvd_app()
            elif my_inp==2:
                self.examine.dvd_ex()
                # print('序号/t/t状态/t/t名称/t/t/t借出日期/t/t借出次数')
                # print('{0}/t/t{1}/t/t{2}/t/t/t{3}/t/t{4}'.format(1,1,1,1,1))
                # print(lst)
                # print('*'*20)
            elif my_inp==3:
                self.D_del.dvd_del()
            elif my_inp==4:
                self.loan.dvd_loan()
            elif my_inp==5:
                # self.D_return.dvd_return()
                self.name = input('请输入DVD名称： ')
                lst.append(self.name)
                self.return_data = int(input('请输入归还日期：'))
                print('归还《%s》成功！'% self.name)
                print('借出日期为：%d'%d_loan.loan_data)
                print('归还日期为：%d'%self.return_data)
                self.money = (self.return_data - d_loan.loan_data) * 1
                print('应付租金（元）：%d' % self.money)
            elif my_inp==6:
                print('谢谢使用')
                break

d_append=DVD_append('天龙八部')
d_examine=DVD_examine(1,1,'<<万古至尊>>',1,1)
d_del=DVD_del('天龙八部')
d_loan=DVD_loan('天龙八部',1)
d_return=DVD_return('天龙八部',2,2)
d_quit=DVD_quit()
d_dvd=DVD(d_append,d_examine,d_del,d_loan,d_return,d_quit)
d_dvd.DVD_system()

