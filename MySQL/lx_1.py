import pymysql
# 连接MySQL数据库，  本机         用户名   密码      数据库名
db=pymysql.connect('localhost','root','123456','zuoye')
# 获取光标
cursor=db.cursor()
# 执行MySQL语句
cursor.execute('select version()')
# 获取下一个查询结果集
data=cursor.fetchone()
print('database version :%s'%data)
db.close()