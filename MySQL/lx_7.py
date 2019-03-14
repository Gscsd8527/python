import pymysql
# 连接MySQL数据库，  本机         用户名   密码      数据库名
db=pymysql.connect('localhost','root','123456','zuoye')
# 获取光标
cursor=db.cursor()
sql="select * from tan WHERE id>1"
try:
    cursor.execute(sql)
    # rowcount:返回执行execute（）方法后影响的行数
    results=cursor.rowcount
    print('影响了%d行'%results)
except:
    print('ERROR:unble to fecth data')
db.close()
