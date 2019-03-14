def test(mystr):
    str_len = len(mystr)
    temp_len = str_len//2
    print(temp_len)
    if mystr[:temp_len+1] == mystr[-temp_len-1:][::-1]:
        print(mystr[:temp_len])
        print(mystr[-temp_len:])
        print('是回文')
        return True
    else:
        print('不是回文')
        return False
mystr='123321'
tan = test(mystr)
print(tan)

