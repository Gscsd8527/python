import json
import datetime
lst = [
    {'app_id':'fcar','method':'Td','channel_type':'0','total': 2, 'reje':1},
    {'app_id':'mmc','method':'a','channel_type':'0','total': 2, 'reje':1},
    {'app_id':'cc','method':'b','channel_type':'0','total': 2, 'reje':1},
]
a = {'app_id':'fcar','method':'Td','channel_type':'0','total': 4, 'reje':2}
for i in lst:
    if a['app_id'] == i['app_id']:
        if a['method'] == i['method']:
            if a['channel_type'] == i['channel_type']:
                i['total'] += a['total']
                i['reje'] += a['reje']
print(lst)


date_start = datetime.datetime.today()-datetime.timedelta(days=1)
print(date_start)

# tt = []
# if tt is not None:
#     print('====')
# if len(tt):
#     print('====')
# elif tt is not None:
#     print('----')

# tt = []
# if len(tt):
#     print('====')
# else:
#     print('----')
# tt = []
# if len(tt) == None:
#     print('====')
# else:
#     print('---')
# print(len(tt))


a=set(range(5))
b=set(range(2,9))
c = a&b
print('cccc',c)
for i in c:
    print(i)

t1 = 'isTDRead'
import re
tp = re.findall('is(.*)Read',t1)
print('tp==',tp)



lt = []
if len(lt) == 0:
    print('333333333')
else:
    print('6666666666')


f = {2,3}
f.add('44')
print(f)


print('------------------')
tp = []
lst_a = {'isTrRead','isttRead','isPyReject'}
for i in lst_a:
    if i.endswith('Read'):
        a = i[2:-4]
        print(a)
        tp.append(a)
print(tp)

print('=============')
tanzhenhua = []
abc = {
    'a': 20,
    'b':23
}
for i in range(5):
    bbb = {
        'c': i,
        'd':i
    }
    abc.update(bbb)
    tanzhenhua.append(abc)
print(tanzhenhua)

print('++++++++++++++++++++++')

tan = []
tt = ['123','456']
for i in range(5):
    t1 = [i,i]
    print(type(t1))
    tt.extend(t1)
    tan.append(tt)
    tt = tt[:2]
print(tan)
import random
for i in tan:
    i[3] += random.random()
print('---',tan)

print(')))))))))))))))))))))))))')
a = [['a','b','c','d','e'],['a','b','c','d','e'],['a','b','c','d','e']]
a = [['a','b','c','d','e']]
add = [i[0] for i in a]
dd = [i[1] for i in a]
bb = [i[2] for i in a]
print('add===',add)
print('dd===',dd)
print('bb===',bb)
