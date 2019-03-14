f=open('G:/pythonfile/tan.txt','rb')
mystr=f.read()
print(mystr)
f.seek(5,0)
# 从初始位置往后移动五个字符，所以输出的位置为5
print(f.tell())
f.seek(5,1)
# 从当前位置往后移动五个字符，因为上面以及移动了五个字符，所以这里的位置为10
print(f.tell())
# 读取所有的字符，所以光标会移动到文件末尾，输出的就是当前的位置：43
f.read()
print(f.tell())
# 从文件末尾往前意义五个字符，43-5=38，所以当前位置为38
f.seek(-5,2)
print(f.tell())



