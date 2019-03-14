import re
mystr='$sdf4'
mre=re.match('.+',mystr)
# print(mre.group())
print(mre.group())
print(mre.pos)
print('-------------------')
st='123abc456def789ghe'
mt=re.match('[0-9]{3}',st)
print(mt.group())
print('-------------')
m='tanzhenhua'
t=re.findall('n',m)
print(t)
p=re.search('n',m)
print(p.group())