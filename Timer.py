import sublime, sublime_plugin
import threading  
import time
import winsound
import csv
from datetime import datetime

i=0
pomodoro_value=0

def show_notification():
    global pomodoro_value
    winsound.PlaySound('C:/Users/kiril/AppData/Roaming/Sublime Text 3/Packages/MyPlugin/Sound_11330.wav', winsound.SND_FILENAME)
    sublime.message_dialog("Eat pomodoro and press [Ctrl+Alt+t]")
    pomodoro_value+=1
    sublime.status_message("Ok, let's move on, press [Ctrl+Alt+t]")


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
        #save_pomodoro()

    def showStatus(self):
        global i
        sublime.status_message(time_manage(i))



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

class gtimerstatusCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        global thread1         
        thread1.showStatus()

