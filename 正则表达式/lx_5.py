import re
mystr='dsazzxzxzxsdsxifpouidfbfgfg120fa1f5ad5faf20ga000adsfaixa'
mytest='xxIxxtttxxLovexxtttxxYouxx'
# a='cva'
# b=re.findall('v*',a)
# print(b)
# >>>['', 'v', '', '']

# a='gfg120'
# b=re.findall('f?',a)
# print(b)
# >>>['', 'f', '', '', '', '', '']

# b=re.findall('zx.*zx',mystr)
# print(b)
# >>>['zxzxzx']

#  .*?非贪婪匹配
# b=re.findall('zx.*?x',mystr)
# print(b)
# >>>['zxzx', 'zxsdsx']

#  .*贪婪匹配
# b=re.findall('zx.*x',mystr)
# print(b)
# >>>['zxzxzxsdsxifpouidfbfgfg120fa1f5ad5faf20ga000adsfaix']

# a=re.findall('xx.*?xx',mytest)
# print(a)
# >>>['xxIxx', 'xxLovexx', 'xxYouxx']

# 括号里是我们需要的
# a=re.findall('xx(.*?)xx',mytest)
# print(a)
# >>>['I', 'Love', 'You']
