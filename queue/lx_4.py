# -*- coding: utf-8 -*-

import telnetlib

print('------------------------connect---------------------------')
# 连接Telnet服务器
try:
    tn = telnetlib.Telnet('125.72.232.167',port='8070',timeout=20)
    print(tn)
except:
    print('失败')
else:
    print('成功')

print('-------------------------end----------------------------')