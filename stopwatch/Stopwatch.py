# ***** GLOBALS  and IMPORTS*****
import tkinter as tk
import time
import datetime
import winsound
from tkinter import *
from tkinter.ttk import *
from threading import *
from time import strftime

running = False
hours, minutes, seconds, milliseconds = 0, 0, 0, 0

# ***** FUNCTIONS *****

# clock function
def time():
    string = strftime('%H:%M:%S %p')
    clock_label.config(text = string)
    clock_label.after(1000, time)

# start function
def start():
    global running
    if not running:
        update()
        running = True

# pause function
def pause():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False

# reset function
def reset():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False
    global hours, minutes, seconds, milliseconds
    hours, minutes, seconds, milliseconds = 0, 0, 0, 0
    stopwatch_label.config(text='00:00:00:00')
    alarm_label.config(text= 'Set Alarm' , font=('Lucida Sans Typewriter', 15))
    split_label.config(text='')
# update stopwatch function
def update():
    global hours, minutes, seconds, milliseconds
    milliseconds += 1
    if milliseconds == 100:
        seconds += 1
        milliseconds = 0
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
    milliseconds_string = f'{milliseconds}' if milliseconds > 9 else f'0{milliseconds}'
    stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string + ':' + milliseconds_string )
    global update_time
    update_time = stopwatch_label.after(1, update)

# split function
def split():
    lap = {}
    global running
    global hours, minutes, seconds, milliseconds
    hours_string = f'{hours}'
    minutes_string = f'{minutes}'
    seconds_string = f'{seconds}'
    milliseconds_string = f'{milliseconds}'
    if running:
        lap = hours_string + ':' + minutes_string + ':' + seconds_string + ':' + milliseconds_string
    split_label.config(text='split: ' + lap)

# threading function
def Threading():
    t1=Thread(target = alarm)
    t1.start()

# alarm function
def alarm():
    import time
    while True:
        set_alarm_time = f"{hour1.get()}:{minute1.get()}:{second1.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)
        if current_time == set_alarm_time:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            alarm_label.config(text='TIME IS UP' , font=('Lucida Sans Typewriter', 40))
            return

        

# ***** WIDGETS *****
root = tk.Tk()
root.geometry('725x350')
root.title('Stopwatch')
root.config(bg='#07092c')



#clock
clock_label = tk.Label(font=('Lucida Sans Typewriter', 40), bg='#07092c', fg='white')
clock_label.pack(anchor = 'center')
time()

#stopwatch
stopwatch_label = tk.Label(text='00:00:00:00', font=('Lucida Sans Typewriter', 80), bg='#07092c', fg='white')
stopwatch_label.pack()
split_label = tk.Label (text = '' + '', font = ('Lucida Sans Typewriter', 15), bg='#07092c', fg='white')
split_label.pack()

#alarm
frame = Frame(root)
frame.pack()
alarm_label = tk.Label(text='SET ALARM', font=('Lucida Sans Typewriter', 15), bg='#07092c', fg='white')
alarm_label.pack()

# ***** ALARM SYSTEM ******

hour1 = StringVar(root)
hours1 = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
hour1.set(hours1[0])
 
hrs = OptionMenu(frame, hour1, *hours1)
hrs.pack(side = LEFT)
 
minute1 = StringVar(root)
minutes1 = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute1.set(minutes1[0])
 
mins = OptionMenu(frame, minute1, *minutes1)
mins.pack(side = LEFT)
 
second1 = StringVar(root)
seconds1= ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second1.set(seconds1[0])
 
secs = OptionMenu(frame, second1, *seconds1)
secs.pack(side = LEFT)

# ***** BUTTONS *****

# start, pause, reset, quit buttons
start_button = tk.Button(text='START', height=5, width=7, font=('Lucida Sans Typewriter', 20), command=start, bg='#10195a', fg='white')
start_button.pack(side=tk.LEFT)
pause_button = tk.Button(text='PAUSE', height=5, width=7, font=('Lucida Sans Typewriter', 20), command=pause, bg='#10195a', fg='white')
pause_button.pack(side=tk.LEFT)
reset_button = tk.Button(text='RESET', height=5, width=7, font=('Lucida Sans Typewriter', 20), command=reset, bg='#10195a', fg='white')
reset_button.pack(side=tk.LEFT)
split_button = tk.Button(text='SPLIT', height=5, width=7, font=('Lucida Sans Typewriter', 20), command=split, bg='#10195a', fg='white')
split_button.pack(side=tk.LEFT)
alarm_button = tk.Button(text='ALARM', height=5, width=7, font=('Lucida Sans Typewriter', 20), command=alarm, bg='#10195a', fg='white')
alarm_button.pack(side=tk.LEFT)
quit_button = tk.Button(text='QUIT', height=5, width=7, font=('Lucida Sans Typewriter', 20), command=root.quit, bg='#10195a', fg='white')
quit_button.pack(side=tk.LEFT)

root.mainloop()