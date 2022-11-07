from tkinter import*
window=Tk()
window.geometry('800x600')
window.title('14.currecy Converter')
var1=StringVar()
var2=StringVar()
def Convert():
    if(e4.get()):
        lb=Label(window,text=str(float(e4.get())*76.67))
        lb.grid(row=11,column=0)
        lb.configure(font=("Helvetica", 18, "bold"))  
    else:
        lb=Label(window,text=str(float(e5.get()))/76.67)
        lb.grid(row=7,coulum=0)
        lb.configure(font=("Helvetica",18,"bold"))
l1=Label(window,text="Welcome to Real Time Currency Converter",width=55,height=3,bg='Light Green')
l1.grid(row=0,column=0)
l1.configure(font=("Helvetica", 18, "bold"))
le=Label(window).grid(row=1,column=0)
l2=Label(window,text='1 USd=76.67 INR')
l2.grid(row=2,column=0)
l2.configure(font=("Helvetica", 18, "bold"))
l3=Label(window,text='Date: 2022/05/03')
l3.grid(row=3,column=0)
l3.configure(font=("Helvetica", 18, "bold"))
le=Label(window).grid(row=4,column=0)
l4=Label(window,text='USD')
l4.grid(row=5,column=0)
l4.configure(font=("Helvetica", 18, "bold"))
e4=Entry(window)
e4.grid(row=6,column=0)
le=Label(window).grid(row=8,column=0)
l5=Label(window,text='INR')
l5.grid(row=10,column=0)
l5.configure(font=("Helvetica", 18, "bold"))
e5=Entry(window)
e5.grid(row=12,column=0)
b1=Button(window,text="Convert",command=Convert,bg='Blue')
b1.grid(row=15,column=0)
b1.configure(font=("Helvetica", 18, "bold"))
b2=Button(window,text="Close",command=window.destroy,bg='Red')
b2.grid(row=16,column=0)
b2.configure(font=("Helvetica", 18, "bold"))
window.mainloop()


