from  tkinter import*
from tkinter import messagebox
root = Tk()
root.title="Message_box"
lb1=Label(root,text="Price 1")
lb2=Label(root,text="Price 2")
lb3=Label(root,text="Price 3")
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
def total():
    tot=int(e1.get())+int(e2.get())+int(e3.get())
    messagebox.showinfo("Result","total:"+str(tot))
    b1=Button(root,text="total",command=total)
    b1.grid(row=4,column=1)

    mainloop()