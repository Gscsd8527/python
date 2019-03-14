i =1
j = 1
sum = 0
while i<=2:
    print ('please name:')
    name = raw_input()
    i+=1
    while j<=5:
        print ('please input chengji %d'%j)
        sum+=input()
        j+=1
    avg = sum/5
    print('%s de avg zhengji wei:%d'%name %avg)