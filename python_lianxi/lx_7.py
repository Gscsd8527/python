# 100个馒头，大和尚吃三个馒头，小和尚3个人吃一个馒头
# 现求大和尚小和尚有几个
for i in range(1,33):
    for j in range(1,100):
        if i*3+j*(1/3)==100 and i+j==100:
            print(i,j)