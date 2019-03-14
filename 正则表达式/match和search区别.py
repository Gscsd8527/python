import re
a=re.match('super','superstition').span()
print(a)
b=re.match('super','insuperable')
print(b)
c=re.search('super','superstition').span()
print(c)
d=re.search('super','insuperable').span()
print(d)
