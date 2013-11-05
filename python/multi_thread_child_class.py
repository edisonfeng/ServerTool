import time
import threading

class time_print_thread(threading.Thread): #����threading.Thread�������  
    def __init__(self, i_thread_no, i_run_time_interval):  
        threading.Thread.__init__(self)  
        self.i_thread_no=i_thread_no 
        self.i_run_time_interval=i_run_time_interval
        self.i_print_times=0
        self.thread_stop = False  
       
    def run(self): #����run()����,���߳�ִ�еĲ��ַ��ں�����  
        while not self.thread_stop:
            self.i_print_times+=1
            print 'Thread Object %d��%d�����: %s\n' %(self.i_thread_no,self.i_print_times,time.ctime())  
            time.sleep(self.i_run_time_interval)  
    def stop(self):  
        self.thread_stop = True  
             
def test():  
    thread_1 = time_print_thread(1, 3)  
    thread_2 = time_print_thread(2, 2)  
    thread_1.start()  
    thread_2.start()  
    time.sleep(10)  
    thread_1.stop()  
    thread_2.stop()  
    return  
       
if __name__ == '__main__':  
    test()  
