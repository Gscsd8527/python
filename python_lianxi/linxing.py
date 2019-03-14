for i in range(1,6):
    if i<=3:
      for k in range(1,4-i):
         print(end=' ')
      for t in range(1,i+1):
         print('*',end=' ')
      print()
    else:
        for a in range(3,i):
            print(end=' ')
        for b in range(3,8-a):
            print('*',end=' ')
        print()
