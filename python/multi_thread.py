import time  
import thread

def thread_run(i_thread_no,i_run_time_interval): 
    i_print_times = 0
    while i_print_times<5:
        time.sleep(i_run_time_interval)
        i_print_times+=1
        #����������̰߳�ȫ
        print 'Thread_%d��%d�����:%s\n'%(i_thread_no,i_print_times,time.ctime())    
    thread.exit_thread()  
   
def test(): #���������߳�  
    thread.start_new_thread(thread_run, (1,3))#�����̡߳�ִ�к�����+�����в�����  
    thread.start_new_thread(thread_run, (2,3))

test()
