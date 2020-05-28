import datetime
from tkinter import *
from playsound import playsound

#   1:  preguntar tiempo del cronometro (primero hora, luego minutos) //segundos??
#   2:  obtener fecha actual
#   3:  obtener fecha en la que debería sonar la alarma
#   4:  esperar a que coincidad
#     

#0: menu principal, 1 set alarm, 2 change alarm
program_state = 0
tune_path = '/home/emotik811/Music/Nokia ringtone arabic.mp3'
#VENTANA#
window = Tk()
window.title('Simple Alarm')
window.geometry('350x200')



#ETIQUETAS#
label_path = Label(window,text='Tune: '+tune_path,font=('Arial Bold',12))
label_path.grid(column=0,row=0)

#TEXTO#

#FUNCIONES#

def button_set_alarmn_clicked():

    set_alarm_window =Tk()
    set_alarm_window.title('Simple Alarm: Set Alarm')


    text_hours = Entry(set_alarm_window, width=8)
    text_minutes=Entry(set_alarm_window,width=8)
    text_seconds=Entry(set_alarm_window, width=8)
    
    label_hours = Label(set_alarm_window,text='Hours: ')
    label_hours.grid(column=0,row=1)
    label_minutes = Label(set_alarm_window,text='Minutes: ')
    label_minutes.grid(column=0,row=2)
    label_seconds = Label(set_alarm_window,text='Seconds: ')
    label_seconds.grid(column=0,row=3)

    text_hours.grid(column=1,row=1)
    text_minutes.grid(column=1,row=2)
    text_seconds.grid(column=1,row=3)

    set_alarm_window.mainloop()
#BOTONES#
button_set_alarm = Button(window,text='Set Alarm', font=('Arial Bold',12),command=button_set_alarmn_clicked)
button_set_alarm.grid(column = 0, row=1)

button_change_tune = Button(window,text='Change Alarm Tune',font=('Arial Bold',12))
button_change_tune.grid(column = 0, row=2)
window.mainloop()

def control():

    option = -1

    while option !='0':

        print('Exit: (0)')
        print('Set alarm: (1)')
        print('Change alarm tune: (2) [Actual tune: '+tune_path+']')
        option = input('Choose an option: ')

        if option == '1':
            set_alarm()
        if option == '2':
            set_alarm_tune()
            print(tune_path)
        if option == '0':
            print('Closing...')
        else:
            print('No valid option')

def set_alarm():
    tiempo_alarma = introduce_values()

    diferencia = tiempo_alarma - datetime.datetime.now()

    while diferencia.days>=0:
        print(diferencia)
        diferencia = tiempo_alarma - datetime.datetime.now()

    print("ALARMA SUENA")
    playsound(tune_path)

def introduce_values():

    hour =input("Introzuca horas: ")
    minutes = input("Introduzca minutos: ")
    seconds = input("Introduzca segundos: ")
    date = datetime.datetime.now() + datetime.timedelta(hours=float(hour), minutes=float(minutes), seconds=float(seconds))
    return date

def set_alarm_tune():
    global tune_path
    new_tune_path = input('Select path: ')
    tune_path = new_tune_path


window = tkinter.Tk()
window.mainloop()

#control()


