from tkinter import *
from tkinter.ttk import *
import time
window=Tk()
window.geometry('450x350')
window.title('15. Progressbar')
def run():
    progress.start()
def startp():
        for x in range (5):
            progress['value']+=20
            window.update_idletasks()
            time.sleep(1)
            print(progress['value'])
def stop_i():
    progress.stop()
def stop_s():
    a=progress['value']
    if(progress['value']==a+1):
        progress.stop()
progress = Progressbar(window, orient = HORIZONTAL,length = 100, mode = 'determinate')
progress.grid(row=4,column=2)
le=Label(window,width=5).grid(row=0,column=0)
b1=Button(window,text='Run Progress Bar',command=run).grid(row=0,column=1)
le=Label(window,width=5).grid(row=0,column=2)
b2=Button(window,text='Start Progress Bar',command=startp).grid(row=0,column=3)
le=Label(window,width=5).grid(row=1,column=0)
b3=Button(window,text='Stop Immediately',command=stop_i).grid(row=2,column=1)
b4=Button(window,text='Stop after Second',command=stop_s).grid(row=2,column=3)
le=Label(window).grid(row=3,column=0)
window.mainloop()