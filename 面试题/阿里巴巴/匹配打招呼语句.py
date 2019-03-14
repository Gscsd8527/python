import re
str = '''hello,Tom
         你好,吉米
         你在干嘛
         我在打游戏呢
         好玩吗
         挺好玩的
         good monery
         早
         '''
com = '[H,h]ello|[H,h]i|[你,您]好|嗨|good.*|早'
res = re.findall(com,str)
print(res)
