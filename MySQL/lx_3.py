import pymysql
# 连接MySQL数据库，  本机         用户名   密码      数据库名
db=pymysql.connect('localhost','root','123456','zuoye')
# 获取光标
cursor=db.cursor()
sql='''
insert into tan VALUES (1,'xiaowang'),(2,'xiaozhang'),(3,'xiaotan')
'''
try:
    cursor.execute(sql)
    # 提交到数据库中去执行
    db.commit()
except:
    # 回滚（返回原来的状况）
    db.rollback()
db.close()