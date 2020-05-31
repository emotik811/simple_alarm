import datetime
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from playsound import playsound


tune_path = 'E:\juanr\Music\Memento Mori\Dreadnaught.mp3'

#States: no_time, playing, pause
program_state = 'no_time'

#Default: font, font size, font color, background color
font = 'Arial Bold'
font_size = 12

#VENTANA#
window = Tk()
window.title('Simple Alarm')
window.geometry('350x200')




#TUNE#
#label_path = Label(window,text='Tune: '+tune_path,font=(font,font_size))
#label_path.grid(column=1,row=0)
#change_tune_botton = Button(window, text='Change')
#change_tune_botton.grid(column=0,row=0)

#TIME#
fc=1
if program_state == 'no_time':
    
    entry_hours = Entry(window,width=6)
    entry_hours.insert(0,'1')
    entry_hours.grid(column =fc , row=3 )
    dpl_1 = Label(window,text=':')
    dpl_1.grid(column=fc+1,row=3)
    entry_minutes = Entry(window,width=6)
    entry_minutes.insert(0,'0')
    entry_minutes.grid(column =fc+2, row=3)
    dpl_2 = Label(window,text=':')
    dpl_2.grid(column=fc+3,row=3)
    entry_seconds = Entry(window,width=6)
    entry_seconds.insert(0,'0')
    entry_seconds.grid(column=fc+4,row=3)
else:
    remaining_hours = Label(window,width=6,text='h')
    remaining_hours.grid(column =fc , row=3 )
    dpl_1 = Label(window,text=':')
    dpl_1.grid(column=fc+1,row=3)
    remaining_minutes = Label(window,width=6,text='m')
    remaining_minutes.grid(column =fc+2, row=3)
    dpl_2 = Label(window,text=':')
    dpl_2.grid(column=fc+3,row=3)
    remaining_seconds = Entry(window,width=6,text='s')
    remaining_seconds.grid(column=fc+4,row=3)

label_state = Label(text=program_state)
label_state.grid(column = 0, row = 6)

def play_button_click():
    global program_state
    if program_state == 'no_time':
        hours = entry_hours.get()
        minutes = entry_minutes.get()
        seconds = entry_seconds.get()
        #time_alarm = datetime.datetime.now() + datetime.timedelta(hours=float(hours), minutes=float(minutes), seconds=float(seconds))
        program_state ='playing'
        
    else:
        program_state = 'playing_2'   

    print(program_state) 
    #difference = time_alarm - datetime.datetime.now()

    #while difference.days>=0:
     #   print(difference)
      #  difference = time_alarm - datetime.datetime.now()

play_button = Button(window, text='Play',command=play_button_click)
play_button.grid(column=fc+2,row=4)


def set_alarm_tune():
    global tune_path
    new_tune_path = input('Select path: ')
    tune_path = new_tune_path


window.mainloop()



#control()


