import os, sys, string
import MySQLdb

i_staff_no_start=222
i_staff_no_end=555

try:
    conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='feng',db='test')
except Exception, e:
    print e
    sys.exit()

cursor=conn.cursor()        
cursor.execute('call python_pro_dataset(%s,%s)',(i_staff_no_start,i_staff_no_end))   
data=cursor.fetchall()   
if data:
    for rec in data:   
        print rec[0],rec[1]
        cursor.nextset()

cursor.close()
conn.close()
