from tkinter import*
from tkinter import messagebox

root =Tk()
root.geometry("300x200")
root.title="pythonGuideas"

lb1=Label(root,text="file name")
lb2=Label(root,text="Email")
lb3=Label(root,text="pass")

e1=Entry(root)
e2=Entry(root)
e3=Entry(root)


b1=Button(text="insert")
b2=Button(text="delete")
b3=Button(text="Update")
b4=Button(text="Select")
spin=Spinbox(from_=0,to=25)

rb1=Radiobutton(text="female",value=1)
rb2=Radiobutton(text="MAle",value=2)
rb3=Radiobutton(text="other",value=3)

cb1=Checkbutton(root,text='Accept terms and condition')

lb1.grid(row=1,column=1)
lb2.grid(row=2,column=1)
lb3.grid(row=3,column=1)
e1.grid(row=1,column=2)
e2.grid(row=2,column=2)
e3.grid(row=3,column=2)
rb1.grid(row=4,column=2)
rb2.grid(row=5,column=2)
rb3.grid(row=6,column=2)
cb1.grid(row=7,column=2)

b4.grid(row=8,column=2)

root.mainloop()
