my_file004=open('D:\\ProgramData\\python\\file004.txt', 'r+')
my_file004.seek(0)#���ļ���ͷ��ȡ
my_file004_content=my_file004.read()
my_file004.close()
print '���ļ���ͷ��ȡ���������ݣ� \n',my_file004_content

my_file004=open('D:\\ProgramData\\python\\file004.txt', 'r+')
my_file004.seek(2,0)#0����ʾ���ļ�ͷ��ʼ  2������ƫ��2λ
my_file004_content=my_file004.read(7)#��ȡ��ǰλ�ú����7���ַ����������з���
my_file004.close()
print '�������ݣ� \n',my_file004_content

my_file004=open('D:\\ProgramData\\python\\file004.txt', 'r+')
my_file004.seek(-2,2)#2�����ļ�ĩβ��ʼ  -2������ƫ��2λ
my_file004_content=my_file004.read()
my_file004.close()
print '�������ݣ� \n',my_file004_content




