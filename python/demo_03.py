my_file004=open('D:\\ProgramData\\python\\file004.txt', 'r+')
my_file004.seek(0)#从文件开头读取
my_file004_content=my_file004.read()
my_file004.close()
print '从文件开头读取的完整内容： \n',my_file004_content

my_file004=open('D:\\ProgramData\\python\\file004.txt', 'r+')
my_file004.seek(2,0)#0：表示从文件头开始  2：向右偏移2位
my_file004_content=my_file004.read(7)#读取当前位置后面的7个字符（包括换行符）
my_file004.close()
print '部分内容： \n',my_file004_content

my_file004=open('D:\\ProgramData\\python\\file004.txt', 'r+')
my_file004.seek(-2,2)#2：从文件末尾开始  -2：向左偏移2位
my_file004_content=my_file004.read()
my_file004.close()
print '部分内容： \n',my_file004_content




