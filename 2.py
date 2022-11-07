from tkinter import*
from tkinter import messagebox
root=Tk()
root.title=("billing")

lb1=Label(root,text="NAme:")
lb2=Label(root,text="product:")
lb3=Label(root,text="quantity:")

e1=Entry()
e2=Entry()
e3=Entry()

lb1.grid(row=1, column=1)
lb2.grid(row=2, column=1)
lb3.grid(row=3, column=1)

e1.grid(row=1,column = 2)
e2.grid(row=2,column = 2)
e3.grid(row=3,column = 2)

text_box=Text(root,height=10,width=30)
text_box.place(x=5,y=130)

b1 = Button(root, text="Add Item")
b2 = Button(root, text="Clear Items")
b3 = Button(root, text="Total Items")
b1.grid(row=4,column=2)
b2.place(x=5,y=310)
b3.place(x=200,y=310)

mainloop()
