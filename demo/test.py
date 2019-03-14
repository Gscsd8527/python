import pandas
import datetime
# date = pandas.date_range(start='20110101', end='20190114')
# print(date.values)

date_set = set()
url_list = []
now = datetime.datetime.today()
start_date = '2011-01-01'
start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
while start_date < now:
    start_date = start_date + datetime.timedelta(days=1)
    date_set.add(start_date.strftime('%Y-%m'))
date_set = sorted(date_set)
for date in date_set:
    temp_month = date[5:]
    if date < '2016-01-03':
        if temp_month[0] == '0':
            date = date[:4] + temp_month[1]
        else:
            date = date[:4] + temp_month
        url = 'http://tianqi.2345.com/t/wea_history/js/54511_{}.js'.format(date)
    else:
        date = date[:4] + temp_month
        url = 'http://tianqi.2345.com/t/wea_history/js/{}/54511_{}.js'.format(date, date)
    url_list.append(url)
# for url in url_list:
#     print(url)


# start_date = pandas.datetime.strptime('2011-01-01', '%Y-%m-%d').strftime('%Y-%m-%d')
# start_date = '2011-01-01'
# end_date = pandas.datetime.now().strftime('%Y-%m-%d')
# df = pandas.date_range(start=start_date, end=end_date)


# print(type(df))
# df = df.apply(lambda x: x[:7])
# print(df)


# import datetime
# today = datetime.datetime.now()
# yesterday = today - datetime.timedelta(days=1)
# # print(yesterday.strftime('%Y%m%d00'))
# # start_day = yesterday.strftime('%Y%m%d') + "00"
# start_day = yesterday.strftime('%Y%m%d')
# print(type(start_date))
# start_date = start_day + '00'
# print(start_date)
#
# a = "it's pig"
# b = 'it"s pig'
# print(a)
# print(b)


# a1 = [1, 2]
# a2 = [3, 4]
# b = [4, 5]
# c = [5, 6]
# a1.append(b)
# print(a1)
# a2.extend(c)
# print(a2)

a = [1, 2, 3, 4, 5]
# print('a=', a)
# b = a
# b[1] = 10000
# print(a)
# print(b)
# b = a.copy()
b = a[:]
b[1] = 1000
print(a)
print(b)
