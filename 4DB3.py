from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("900x700")
lbl1=Label(root,text="JOB APPLICATION",font=("Arial", 25))
lbl1.grid(row=1,column=2)
lbl2=Label(root,text="PERSONAL INFORMATION",fg="RED",font=("Arial", 15))
lbl2.grid(row=2,column=1)
lbl3=Label(root,text="Name")
lbl3.grid(row=3,column=1)
e1=Entry(root)
e1.grid(row=3,column=2)
e2=Entry(root)
e2.grid(row=3,column=3)
lbl4=Label(root,text="First Name")
lbl4.grid(row=4,column=2)
lbl5=Label(root,text="Last Name")
lbl5.grid(row=4,column=3)
lbl6=Label(root,text="Email")
lbl6.grid(row=5,column=1)
e3=Entry(root)
e3.grid(row=5,column=2)
lbl7=Label(root,text="Education")
lbl7.grid(row=6,column=1)
lbl8=Label(root,text="Resume")
lbl8.grid(row=7,column=1)
lbl9=Label(root,text="Address")
lbl9.grid(row=8,column=1)
e4=Entry(root)
e4.grid(row=8,column=2)
lbl10=Label(root,text="Address1")
lbl10.grid(row=9,column=2)
e5=Entry(root)
e5.grid(row=10,column=2)
lbl11=Label(root,text="Address2")
lbl11.grid(row=11,column=2)
lbl12=Label(root,text="Country")
lbl12.grid(row=13,column=2)
e6=Entry(root)
e6.grid(row=14,column=2)
e7=Entry(root)
e7.grid(row=14,column=3)
e8=Entry(root)
e8.grid(row=14,column=4)
lbl13=Label(root,text="City")
lbl13.grid(row=15,column=2)
lbl14=Label(root,text="State")
lbl14.grid(row=15,column=3)
lbl15=Label(root,text="Pincode")
lbl15.grid(row=15,column=4)
lbl16=Label(root,text="Phone Number")
lbl16.grid(row=16,column=1)
e8=Entry(root)
e8.grid(row=16,column=2)
e9=Entry(root)
e9.grid(row=16,column=3)
lbl17=Label(root,text="What are your hobbies?")
lbl17.grid(row=17,column=1)
e10=Entry(root)
e10.grid(row=18,column=1)
lbl18=Label(root,text="Precious/Current Employment Details",fg="RED",font=("Arial", 15))
lbl18.grid(row=19,column=1)
lbl19=Label(root,text="Company Name")
lbl19.grid(row=20,column=1)
lbl20=Label(root,text="Job Title")
lbl20.grid(row=21,column=1)
lbl21=Label(root,text="How long were you here?")
lbl21.grid(row=22,column=1)
e11=Entry(root)
e11.grid(row=20,column=2)
e12=Entry(root)
e12.grid(row=21,column=2)
e13=Entry(root)
e13.grid(row=22,column=2)
lbl22=Label(root,text="Reference #1",fg="RED",font=("Arial", 15))
lbl22.grid(row=23,column=1)
lbl23=Label(root,text="Name")
lbl23.grid(row=24,column=1)
lbl24=Label(root,text="Phone")
lbl24.grid(row=25,column=1)
e14=Entry(root)
e14.grid(row=24,column=2)
e15=Entry(root)
e15.grid(row=25,column=2)
lbl25=Label(root,text="Reference #2",fg="RED",font=("Arial", 15))
lbl25.grid(row=26,column=1)
lbl26=Label(root,text="Name")
lbl26.grid(row=27,column=1)
lbl27=Label(root,text="Phone")
lbl27.grid(row=28,column=1)
e16=Entry(root)
e16.grid(row=27,column=2)
e17=Entry(root)
e17.grid(row=28,column=2)
btn1=Button(root,text="Apply")
btn1.grid(row=31,column=2)
mainloop()