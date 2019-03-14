my_inp=int(input('请你输入月份：'))
while 1:
    if my_inp==2:
        my_year=int(input('请输入年份：'))
        if(my_year%100!=0 or my_year%4==0 or my_year%400==0):
            print('当前月份为：',2,'月',"该月有28天")
        else:
            print('当前月份为：', 2,'月', "该月有29天")
    if my_inp in [1,3,5,7,8,10,12]:
        print('当前月份为：', my_inp,'月', "该月有31天")
    if my_inp in [4,6,9,11]:
        print('当前月份为：', my_inp,'月', "该月有30天")
    break
