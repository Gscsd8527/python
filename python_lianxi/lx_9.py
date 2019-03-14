# 公鸡5文钱一只，母鸡3文钱一只，小鸡3只一文钱，用100文钱买100只鸡，如何买？
for i in range(1,20):
    for j in range(1,33):
        for k in range(1,300):
            if i+j+k==100 and 5*i+j*3+k*(1/3)==100:
                print(i,j,k)