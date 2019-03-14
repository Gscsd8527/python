import re
mystr='tanzhenhuatan'
test=re.match('tan',mystr)
print(test.group())
# 返回匹配的所有字符串，并生成一个列表
print(re.findall('tan',mystr))
# 匹配末尾的字符串的下标
print(test.end())
# 匹配第一个字符串的下标
print(test.start())
# 定位匹配字符串的第一个位置
print(test.pos)