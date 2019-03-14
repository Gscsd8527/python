import re
s='asdfxxIxx123xxLovexxdfd'
f = re.search('xx(.*?)xx123xx(.*?)xx',s).group(2)
print(f)