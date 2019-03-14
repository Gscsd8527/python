# 写出开头匹配字母和下划线，末尾是数字的正则表达式
import re
a='a_afasf2323'
b='_a4334sf2323'
c='4334sf2323fg'
mystr=re.findall('^[A-Za-z_]|_.*\d$',a)
print(mystr)