import pymysql
# 连接MySQL数据库，  本机         用户名   密码      数据库名
db=pymysql.connect('localhost','root','123456','zuoye')
# 获取光标
cursor=db.cursor()
sql="update tan set tan_name='xiaoming' WHERE id=3"
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
