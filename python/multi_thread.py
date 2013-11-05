import time  
import thread

def thread_run(i_thread_no,i_run_time_interval): 
    i_print_times = 0
    while i_print_times<5:
        time.sleep(i_run_time_interval)
        i_print_times+=1
        #输出操作非线程安全
        print 'Thread_%d第%d次输出:%s\n'%(i_thread_no,i_print_times,time.ctime())    
    thread.exit_thread()  
   
def test(): #创建两个线程  
    thread.start_new_thread(thread_run, (1,3))#传递线程“执行函数”+“所有参数”  
    thread.start_new_thread(thread_run, (2,3))

test()
