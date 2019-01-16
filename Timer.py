import sublime, sublime_plugin
import threading  
import time

i=0
def show_notification():
    #playsound.playsound('Sound_11330.wav', True)
    #winsound.PlaySound("Sound_11330.wav", winsound.SND_ASYNC)
    sublime.message_dialog("Drink some water")
    sublime.status_message("Drink some water")
    
def write_time():
    sublime.status_message(time_manage(i))

def time_manage(time_number):
    time_str='    time:    '+str(int(time_number/60))+'min '+str(time_number%60)+'s'
    return time_str

class timer(threading.Thread):
    def __init__(self, num, interval):
        threading.Thread.__init__(self)
        self.thread_num = num
        self.interval = interval
        self.thread_stop = False 
    def run(self):
        global i
        while not self.thread_stop:
            sublime.set_timeout(write_time, 1)
            i+=1  
            if i % 30 == 0:
                show_notification()
                self.pause()
            time.sleep(self.interval)          
    def pause(self):        
        self.thread_stop = True
    
    def zeroing(self):
        global i
        i=0    



thread1 = timer(1, 1)





class gtimerCommand(sublime_plugin.TextCommand):    
    def run(self, edit):
        global thread1
        thread=timer(1,1) 
        if not thread1.isAlive():                              
            thread.start()
            thread1=thread


class gtimerpauseCommand(sublime_plugin.TextCommand):    
    def run(self, edit):         
        global thread1
        thread1.pause()

class gtimerzeroCommand(sublime_plugin.TextCommand):    
    def run(self, edit):
        global thread1         
        thread1.zeroing()
        
