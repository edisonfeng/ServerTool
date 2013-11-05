import os, sys, string
import MySQLdb

i_staff_no=222
v_staff_name=''

try:
    conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='feng',db='test')
except Exception, e:
    print e
    sys.exit()
       
cursor=conn.cursor()   
cursor.callproc('python_pro_param',(i_staff_no,v_staff_name))   
cursor.execute('select @_python_pro_param_0,@_python_pro_param_1')#0:第一个参数
data=cursor.fetchall()                                            #1:第二个参数
if data:
    for rec in data:     
        v_staff_name=rec[1]   
        print i_staff_no,v_staff_name

cursor.close()
conn.close()
