import os, sys, string
import MySQLdb

#�������ݿ�
try:
    conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='feng',db='test')
except Exception, e:
    print e
    sys.exit()
# ��ȡcursor���������в���
cursor = conn.cursor()

#���뵥������
sql = "insert into user_info(i_id,v_name) values (%d, '%s')"%(333,"ccc")
try:
    cursor.execute(sql)
except Exception, e:
    print e
#�����������
sql = "insert into user_info(i_id,v_name) values (%s, %s)"#�˴�����%s����
val = ((444,"ddd"),(555,"eee"), (666,"fff"))
try:
    cursor.executemany(sql, val)
except Exception, e:
    print e

#��ѯ����
sql= "select * from user_info order by i_id"
cursor.execute(sql)
alldata = cursor.fetchall()
# ��������ݷ��أ���ѭ�����, alldata���и���ά���б�
if alldata:
    for rec in alldata:
        print rec[0], rec[1]

cursor.close()
conn.close()
    
    

