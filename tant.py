# import requests
# from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
# import random
# import json
# search = '神州优车'
# a = 'https://m.weibo.cn/api/container/getIndex?type=all&queryVal={}&featurecode=20000320&luicode=10000011&lfid=106003type%3D1&title={}&containerid=100103type%3D1%26q%3D{}&page=1'.format(search,search,search)
# ua = UserAgent()
# headers = {
#     'User-Agent': ua.random,
#     'Cookie': 'SINAGLOBAL=133986724540.59125.1515238775247; login_sid_t=40bf30d0da845252b384d50e3a065563; SWBSSL=usrmdinst_13; _s_tentry=www.so.com; Apache=1876920433714.9858.1534212589544; ULV=1534212589550:20:5:3:1876920433714.9858.1534212589544:1534168659553; SWB=usrmdinst_8; WBtopGlobal_register_version=2b2691ab11833cbd; cross_origin_proto=SSL; UOR=baoku.360.cn,widget.weibo.com,www.so.com; SSOLoginState=1534239219; SCF=ApqnCMUkPZc9EI17Xvjp0jkkQKbUMjPi5DDxDdTUsNnaL4cz0NFZDJQZkt8GL94ZMrFPzifqiNeG0UASowxURvk.; SUB=_2A252dtGhDeRhGeNH6lcT8SrKwzuIHXVVAkRprDV8PUJbmtAKLUrAkW9NSsMMu4JOfYAYWSLJKKV8vpc7H3PVVrvT; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhYQBTbQPxe5oBBA9GCvNGD5JpX5K2hUgL.Fo-4eK-EeKBc1hM2dJLoIf2LxKqL1hnL1K2LxK-L12qLB-2LxKqL1h.L1KeLxK.L1h-LBo2LxKqLBozLBo.LxKBLBonL12BLxK.LBKzL1hqLxKML1-zL1KzLxK.LBK-LB-Bt; SUHB=0wn1tTzNQ15IFh; un=14779569000; wvr=6; WBStorage=e8781eb7dee3fd7f|undefined',
# }
# print(a)
# r =requests.get(a,headers=headers).text
# a=json.loads(r)
# print(a)

# a = {'a': '1111','b':'222222','c':'3333333'}
# # b = {'a': 'aaaa', 'b':'bbbbb'}
# b = {'a': 'aaaa', 'b':'bbbbb'}
# if a.get('d', None):
#     print('=======')
# else:
#     print('1111111')


# 北京时间装换成UTC时间
# import datetime
# a = datetime.datetime.today()
# o = datetime.timedelta(hours=8)
# c = (a-o).strftime('%Y-%m-%d %H:%M:%S')
# print(a-o)
# print(c)


# a = '西南风1~2级'
# for i in a:
#     if i.isdigit():
#         print(i)
#         index = a.index(i)
#         break
#     # break
# print('------',index)

start_data = '2015-01-01'
end_data = '2018-08-28'
import datetime
a = datetime.datetime.today()
b = datetime.timedelta(hours=8)
print(a - b)

c = datetime.datetime.strptime(start_data,'%Y-%m-%d')
d = datetime.timedelta(hours=8)
e = c - d
print(e)
print(e.strftime('%Y-%m-%d'))

a4 = [[1,2,3],[1,3,4],[2,2,5],[2,3,3],[3,2,3],[3,3,6],]
a5 = []
temp = []
for i in a4:
    if i[0] not in temp:
        temp.append(i[0])
    if i[0] in temp:
        if i[1] == 2:
            temp.insert(1,i)
        elif i[1] == 3:
            temp.insert(2,i)
    a5.append(temp)
    temp = []
print(a5)

a = []
b = [1,2,3]
a.append(b)
print(a)