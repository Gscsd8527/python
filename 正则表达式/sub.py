import re
s = '123abcssfasdfas123'
output = re.sub('123(.*?)123','123789123',s)
print(output)
