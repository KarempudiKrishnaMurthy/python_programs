from tkinter import *
from tkinter import messagebox
root=Tk()
radio=IntVar()
radio1=IntVar()
root.configure(bg="purple")
lbl1=Label(root,text="STUDENT REGISTRATION FORM")
lbl1.grid(row=1,column=2)
lbl2=Label(root,text="FIRST NAME")
lbl2.grid(row=2,column=1)
e1=Entry(root)
e1.grid(row=2,column=2)
lbl3=Label(root,text="(Max 30 characters a-z and A-Z)")
lbl3.grid(row=2,column=3)
lbl4=Label(root,text="LAST NAME")
lbl4.grid(row=3,column=1)
e2=Entry(root)
e2.grid(row=3,column=2)
lbl5=Label(root,text="(Max 30 characters a-z and A-Z)")
lbl5.grid(row=3,column=3)
lbl6=Label(root,text="DATE OF BIRTH")
lbl6.grid(row=4,column=1)
lbl7=Label(root,text="EMAIL-ID")
lbl7.grid(row=5,column=1)
e3=Entry(root)
e3.grid(row=5,column=2)
lbl8=Label(root,text="MOBILE NUMBER")
lbl8.grid(row=6,column=1)
e4=Entry(root)
e4.grid(row=6,column=2)
lbl9=Label(root,text="GENDER")
lbl9.grid(row=7,column=1)
def choice():
    if(radio.get()==1):
        root.configure(background='')
    elif(radio.get()==2):
        root.configure(background='')
rb1=Radiobutton(root,text="Male", variable=radio,value=1, command=choice)
rb1.grid(row=7,column=2)
rb2=Radiobutton(root,text="Female", variable=radio,value=2, command=choice)
rb2.grid(row=7,column=3)
lbl10=Label(root,text="ADDRESS")
lbl10.grid(row=8,column=1)
T1=Text(root,height=5,width=20)
T1.grid(row=8,column=2)
lbl11=Label(root,text="CITY")
lbl11.grid(row=9,column=1)
e5=Entry(root)
e5.grid(row=9,column=2)
lbl12=Label(root,text="(Max 30 characters a-z and A-Z)")
lbl12.grid(row=9,column=3)
lbl13=Label(root,text="PINCODE")
lbl13.grid(row=10,column=1)
e6=Entry(root)
e6.grid(row=10,column=2)
lbl14=Label(root,text="(6 digit number)")
lbl14.grid(row=10,column=3)
lbl15=Label(root,text="STATE")
lbl15.grid(row=11,column=1)
e7=Entry(root)
e7.grid(row=11,column=2)
lbl16=Label(root,text="(Max 30 characters a-z and A-Z)")
lbl16.grid(row=11,column=3)
lbl17=Label(root,text="COUNTRY")
lbl17.grid(row=12,column=1)
e8=Entry(root)
e8.grid(row=12,column=2)
lbl18=Label(root,text="HOBBIES")
lbl18.grid(row=13,column=1)
v1=IntVar()
v2=IntVar()
v3=IntVar()
v4=IntVar()
v5=IntVar()
cb1=Checkbutton(root,text='Drawing', variable=v1,onvalue=1, offvalue=0)
cb1.grid(row=13,column=2)
cb2=Checkbutton(root,text='Singing', variable=v2,onvalue=1, offvalue=0)
cb2.grid(row=13,column=3)
cb3=Checkbutton(root,text='Dancing', variable=v3,onvalue=1, offvalue=0)
cb3.grid(row=13,column=4)
cb4=Checkbutton(root,text='Sketching', variable=v2,onvalue=1, offvalue=0)
cb4.grid(row=13,column=5)
cb5=Checkbutton(root,text='Others', variable=v3,onvalue=1, offvalue=0)
cb5.grid(row=14,column=2)
e9=Entry(root)
e9.grid(row=14,column=3)
lbl19=Label(root,text="QUALIFICATION")
lbl19.grid(row=15,column=1)
lbl20=Label(root,text="S.NO")
lbl20.grid(row=15,column=2)
lbl21=Label(root,text="EXAMINATION")
lbl21.grid(row=15,column=3)
lbl22=Label(root,text="BOARD")
lbl22.grid(row=15,column=4)
lbl23=Label(root,text="PERCENTAGE")
lbl23.grid(row=15,column=5)
lbl24=Label(root,text="YEAR OF PASSING")
lbl24.grid(row=15,column=6)
lbl25=Label(root,text="1")
lbl25.grid(row=16,column=2)
lbl26=Label(root,text="CLASS X")
lbl26.grid(row=16,column=3)
e10=Entry(root)
e10.grid(row=16,column=4)
e11=Entry(root)
e11.grid(row=16,column=5)
e12=Entry(root)
e12.grid(row=16,column=6)
lbl27=Label(root,text="2")
lbl27.grid(row=17,column=2)
lbl28=Label(root,text="CLASS XI")
lbl28.grid(row=17,column=3)
e13=Entry(root)
e13.grid(row=17,column=4)
e14=Entry(root)
e14.grid(row=17,column=5)
e15=Entry(root)
e15.grid(row=17,column=6)
lbl25=Label(root,text="1")
lbl25.grid(row=16,column=2)
lbl26=Label(root,text="CLASS X")
lbl26.grid(row=16,column=3)
e10=Entry(root)
e10.grid(row=16,column=4)
e11=Entry(root)
e11.grid(row=16,column=5)
e12=Entry(root)
e12.grid(row=16,column=6)
lbl27=Label(root,text="2")
lbl27.grid(row=17,column=2)
lbl28=Label(root,text="CLASS XI")
lbl28.grid(row=17,column=3)
e13=Entry(root)
e13.grid(row=17,column=4)
e14=Entry(root)
e14.grid(row=17,column=5)
e15=Entry(root)
e15.grid(row=17,column=6)
lbl29=Label(root,text="3")
lbl29.grid(row=18,column=2)
lbl30=Label(root,text="CLASS XII")
lbl30.grid(row=18,column=3)
e16=Entry(root)
e16.grid(row=18,column=4)
e17=Entry(root)
e17.grid(row=18,column=5)
e18=Entry(root)
e18.grid(row=18,column=6)
lbl31=Label(root,text="(10 char max)")
lbl31.grid(row=19,column=4)
lbl32=Label(root,text="(Upto 2 decimal)")
lbl32.grid(row=19,column=5)
lbl33=Label(root,text="COURSES APPLIED FOR")
lbl33.grid(row=20,column=1)
def choice1():
    if(radio.get()==1):
        root.configure(background='')
    elif(radio.get()==2):
        root.configure(background='')
    elif(radio.get()==3):
        root.configure(background='')
    elif(radio.get()==4):
        root.configure(background='')
rb3=Radiobutton(root,text="BCA", variable=radio1,value=1, command=choice1)
rb3.grid(row=20,column=2)
rb4=Radiobutton(root,text="B.COM", variable=radio1,value=2, command=choice1)
rb4.grid(row=20,column=3)
rb5=Radiobutton(root,text="B.SC", variable=radio1,value=3, command=choice1)
rb5.grid(row=20,column=4)
rb6=Radiobutton(root,text="B.A", variable=radio1,value=4, command=choice1)
rb6.grid(row=20,column=5)
btn1=Button(root,text="SUBMIT")
btn1.grid(row=26,column=4)
btn2=Button(root,text="RESET")
btn2.grid(row=26,column=5)
mainloop()