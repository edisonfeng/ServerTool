import os, sys, string
import MySQLdb

#连接数据库
try:
    conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='feng',db='test')
except Exception, e:
    print e
    sys.exit()
# 获取cursor对象来进行操作
cursor = conn.cursor()

#插入单条数据
sql = "insert into user_info(i_id,v_name) values (%d, '%s')"%(333,"ccc")
try:
    cursor.execute(sql)
except Exception, e:
    print e
#插入多条数据
sql = "insert into user_info(i_id,v_name) values (%s, %s)"#此处都是%s类型
val = ((444,"ddd"),(555,"eee"), (666,"fff"))
try:
    cursor.executemany(sql, val)
except Exception, e:
    print e

#查询数据
sql= "select * from user_info order by i_id"
cursor.execute(sql)
alldata = cursor.fetchall()
# 如果有数据返回，就循环输出, alldata是有个二维的列表
if alldata:
    for rec in alldata:
        print rec[0], rec[1]

cursor.close()
conn.close()
    
    

