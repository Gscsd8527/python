import re
mystr='hello world'
mysear=re.search('o',mystr)
print(mysear.span())
print(mysear.group(0))
print(mysear.string)
print('-------------')
mst='!@#$efgf152'
t=re.match('.{2}',mst)
print(t.group())