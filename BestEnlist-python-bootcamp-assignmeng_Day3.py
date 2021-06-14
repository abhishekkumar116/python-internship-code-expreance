from tkinter import*

import tkinter.messagebox

window = Tk()

window.title("Employee Registration Form")
window.geometry('300x300')
window.configure(background="blue")

label1 = Label(window, text="Employee Register Form", font=("bold", 31)).grid(row=0, column=2)
FirstName = Label(window, text="FirstName", font=("bold", 15), height=2, width=15).grid(row=1, column=1)
LastName = Label(window, text="LastName", font=("bold", 15), height=2, width=15).grid(row=2, column=1)
Email_Id = Label(window, text="Email_Id", font=("bold", 15), height=2, width=15).grid(row=3, column=1)
Address = Label(window, text="Address", font=("bold", 15), height=2, width=15).grid(row=4, column=1)
City = Label(window, text="City", font=("bold", 15), height=2, width=15).grid(row=5, column=1)
State = Label(window, text="State", font=("bold", 15), height=2, width=15).grid(row=6, column=1)
Country = Label(window, text="Country", font=("bold", 15), height=2, width=15).grid(row=7, column=1)
MobileNo = Label(window, text="Contact Number", font=("bold", 15), height=2, width=15).grid(row=8, column=1)
Gender = Label(window, text="Gender", font=("bold", 15), width=15).grid(row=9, column=1)
var = IntVar()
Radiobutton(window, text="Male", padx=30, font=("bold", 10), variable=var, value=1).grid(row=9, column=2)
Radiobutton(window, text="Female", padx=20, font=("bold", 10), variable=var, value=2).grid(row=9, column=3)

Programming = Label(window, text="Programming", height=2, font=("bold", 15), width=15).grid(row=11, column=1)
var1 = IntVar()
Checkbutton(window, text="java", variable=var1, font=("bold", 10)).grid(row=11, column=2)
var2 = IntVar()
Checkbutton(window, text="python", variable=var2, font=("bold", 10)).grid(row=11, column=3)


FirstName1 = Entry(window).grid(row=1, column=2)
LastName1 = Entry(window).grid(row=2, column=2)
Email_Id1 = Entry(window).grid(row=3, column=2)
City1 = Entry(window).grid(row=5, column=2)
State1 = Entry(window).grid(row=6, column=2)
Country1 = Entry(window).grid(row=7, column=2)
MobileNo1 = Entry(window).grid(row=8, column=2)


def onClick():
    tkinter.messagebox.showinfo("Welcome", "Yor Details Submitted  Successfully !")
Button(window, text="Submit", command=onClick, width=20, bg='brown', fg='white').grid(row=14, column=2)


window.mainloop()

