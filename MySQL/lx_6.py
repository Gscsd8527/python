import pymysql
# 连接MySQL数据库，  本机         用户名   密码      数据库名
db=pymysql.connect('localhost','root','123456','zuoye')
# 获取光标
cursor=db.cursor()
sql="select * from tan WHERE id>1"
try:
    cursor.execute(sql)
    # fetchall:返回第一个结果
    results=cursor.fetchone()
    print('results=  ',results)
    id=results[0]
    name=results[1]
    print('id={0},name={1}'.format(id,name))
except:
    print('ERROR:unble to fecth data')
db.close()
