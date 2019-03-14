import datetime

# 本周
# now = datetime.datetime.now()
# date_start = (now - datetime.timedelta(days=now.weekday())).strftime('%Y-%m-%d')
# date_end = now.strftime('%Y-%m-%d')
# print(date_start)
# print(date_end)

# 上周
# now = datetime.datetime.now()
# date_start = (now - datetime.timedelta(days=now.weekday()+7)).strftime('%Y-%m-%d')
# date_end = (now - datetime.timedelta(days=now.weekday()+1)).strftime('%Y-%m-%d')
# print(date_start)
# print(date_end)

# 本月
# now = datetime.datetime.now()
# date_start = (datetime.datetime(now.year,now.month,1)).strftime('%Y-%m-%d')
# date_end = now.strftime('%Y-%m-%d')
# print(date_start)
# print(date_end)

# 上月
# now = datetime.datetime.now()
# date_end = datetime.datetime(now.year,now.month,1) - datetime.timedelta(days=1)
# date_start = datetime.datetime(date_end.year,date_end.month,1)
# date_start = date_start.strftime('%Y-%m-%d')
# date_end = date_end.strftime('%Y-%m-%d')
# print(date_start)
# print(date_end)


#得到前n天
# now = datetime.datetime.now()
# a = 10
# t = (now - datetime.timedelta(days=a)).strftime('%Y-%m-%d')
# print(t)

#得到前n周
# a=4
# lst = []
# now = datetime.datetime.now()
# while a>=1:
#     date_start = (now - datetime.timedelta(days=now.weekday()))
#     date_end = now.strftime('%Y-%m-%d')
#     lst.append((date_start.strftime('%Y-%m-%d'),date_end))
#     a = a-1
#     while a:
#         date_end = date_start
#         date_start = (date_end - datetime.timedelta(days=7))
#         lst.append((date_start.strftime('%Y-%m-%d'), date_end.strftime('%Y-%m-%d')))
#         a -= 1
# print(lst)


# 得到前n个月的值
# a=4
# lst = []
# now = datetime.datetime.now()
# if a>=1:
#     date_start = datetime.datetime(now.year, now.month, 1)
#     date_end = now.strftime('%Y-%m-%d')
#     lst.append((date_start.strftime('%Y-%m-%d'),date_end))
#     a -= 1
#     while a:
#         date_end = date_start
#         tp = date_end - datetime.timedelta(days=1)  #上一个月的最后一天
#         date_start = datetime.date(tp.year, tp.month, 1) #上一个月的第一天
#         lst.append((date_start.strftime('%Y-%m-%d'), date_end.strftime('%Y-%m-%d')))
#         a -= 1
# print(lst)


# python给定起始和结束日期，如何得到中间所有日期
# import datetime
#
# start = '2018-08-20'
# end = '2018-8-30'
# date = []
# datestart = datetime.datetime.strptime(start, '%Y-%m-%d')
# dateend = datetime.datetime.strptime(end, '%Y-%m-%d')
# print('=====',datestart)
# print('=====',dateend)
# while datestart < dateend:
#     datestart += datetime.timedelta(days=1)
#     date.append(datestart.strftime('%Y-%m-%d'))
# print(date)
# import datetime
#
# now = datetime.datetime.now().strftime('%Y-%m-%d')
# print(now)
# now1 = datetime.datetime.strptime(now, '%Y-%m-%d')
# print(now1)

# a = 'key=faf&adf=adfad&sdfk=asdf&sdfj=hads'
# b = a.replace('&','</br>')
# print(b)
# print(a[-2:])
# c = '09'
# print(int(c))
import json
# dct = "{city:'北京',tqInfo:[{ymd:'2011-01-01',bWendu:'-2℃'}]}"
# dct = "{city:北京,tqInfo:434}"
# dct = json.dumps(dct)
# data = json.loads(dct)
# print(data)
dct = '''
{city:'北京',
tqInfo:[{ymd:'2011-01-01',bWendu:'-2℃',yWendu:'-7℃',tianqi:'多云~阴',fengxiang:'无持续风向',fengli:'微风'},{ymd:'2011-01-02',bWendu:'-2℃',yWendu:'-7℃',tianqi:'多云',fengxiang:'无持续风向',fengli:'微风'},{ymd:'2011-01-03',bWendu:'-2℃',yWendu:'-6℃',tianqi:'多云~阴',fengxiang:'西北风~北风',fengli:'3-4级~4-5级'},{ymd:'2011-01-04',bWendu:'-2℃',yWendu:'-9℃',tianqi:'晴',fengxiang:'北风',fengli:'5-6级'},{ymd:'2011-01-05',bWendu:'-2℃',yWendu:'-10℃',tianqi:'晴',fengxiang:'北风~无持续风向',fengli:'3-4级~微风'},{ymd:'2011-01-06',bWendu:'-1℃',yWendu:'-10℃',tianqi:'晴~多云',fengxiang:'无持续风向',fengli:'微风'},{ymd:'2011-01-07',bWendu:'-1℃',yWendu:'-9℃',tianqi:'多云',fengxiang:'无持续风向~北风',fengli:'微风~3-4级'},{ymd:'2011-01-08',bWendu:'0℃',yWendu:'-9℃',tianqi:'晴',fengxiang:'无持续风向',fengli:'微风'},{ymd:'2011-01-09',bWendu:'0℃',yWendu:'-9℃',tianqi:'晴',fengxiang:'无持续风向',fengli:'微风'},{ymd:'2011-01-10',bWendu:'0℃',yWendu:'-9℃',tianqi:'晴',fengxiang:'无持续风向',fengli:'微风'},{ymd:'2011-01-11',bWendu:'-1℃',yWendu:'-9℃',tianqi:'晴~多云',fengxiang:'无持续风向',fengli:'微风'},{ymd:'2011-01-12',bWendu:'-1℃',yWendu:'-8℃',tianqi:'多云~晴',fengxiang:'北风',fengli:'3-4级'},{ymd:'2011-01-13',bWendu:'-1℃',yWendu:'-9℃',tianqi:'多云',fengxiang:'无持续风向~北风',fengli:'微风~3-4级'},{ymd:'2011-01-14',bWendu:'-2℃',yWendu:'-10℃',tianqi:'晴',fengxiang:'无持续风向',fengli:'微风'},{ymd:'2011-01-15',bWendu:'-2℃',yWendu:'-9℃',tianqi:'晴~多云',fengxiang:'无持续风向',fengli:'微风'},{ymd:'2011-01-16',bWendu:'-1℃',yWendu:'-9℃',tianqi:'阴~晴',fengxiang:'无持续风向',fengli:'微风'},{ymd:'2011-01-26',bWendu:'0℃',yWendu:'-8℃',tianqi:'晴',fengxiang:'无持续风向',fengli:'微风'},{ymd:'2011-01-29',bWendu:'-1℃',yWendu:'-10℃',tianqi:'晴',fengxiang:'无持续风向',fengli:'微风'},{ymd:'2011-01-30',bWendu:'3℃',yWendu:'-7℃',tianqi:'晴',fengxiang:'无持续风向',fengli:'微风'},{ymd:'2011-01-31',bWendu:'7℃',yWendu:'-7℃',tianqi:'晴',fengxiang:'无持续风向',fengli:'微风'},{}],
maxWendu:'7（2011-01-31）',
minWendu:'-10（2011-01-29）',
avgbWendu:'-1',avgyWendu:'-9'}
'''
import json
import re

maxWendu = re.findall("maxWendu:'(.*?)'", dct)[0]
minWendu = re.findall("minWendu:'(.*?)'", dct)[0]
avgbWendu = re.findall("avgbWendu:'(.*?)'", dct)[0]
avgyWendu = re.findall("avgyWendu:'(.*?)'", dct)[0]
print(maxWendu,minWendu,avgbWendu,avgyWendu)


re_city = re.findall('city:(.*?),',dct)[0].strip("'")
every_date1 = re.findall('tqInfo:\[(.*)]',dct)[0]
every_date2 = every_date1.rstrip('{}').rstrip(',')
every_date3 = re.findall('{.*?}',every_date2)

datalist = []
for every in every_date3:
    everyData = every.strip('{}').split(',')
    print('every----',everyData)
    dalist = []
    for eve in everyData:
        da = eve.replace("'",'').split(':')  #"ymd:'2011-01-01'",
        dalist.append(da[1])
    datalist.append(dalist)
print(datalist)


