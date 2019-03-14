import pymysql
# 连接MySQL数据库，  本机         用户名   密码      数据库名
db=pymysql.connect('localhost','root','123456','zuoye')
# 获取光标
cursor=db.cursor()
sql="select * from tan WHERE id>1"
try:
    cursor.execute(sql)
    # fetchall:接收全部的返回结果行
    results=cursor.fetchall()
    print('results=  ',results)
    for row in results:
        print('row= ',row)
        id=row[0]
        name=row[1]
        print('id={0},name={1}'.format(id,name))
except:
    print('ERROR:unble to fecth data')
db.close()