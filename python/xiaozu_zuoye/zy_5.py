# 求1-2+3-4+5 ... 99的所有数的和
my_sum=0
for i in range(1,100):
    if i%2==1:
        my_sum+=i
    if i%2==0:
        my_sum-=i
    print(i,my_sum)
print('1-2+3-4+5 ... 99的所有数的和:',my_sum)
