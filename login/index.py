# import library
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# create window
window = Tk()
window.title('My System - Access Panel')
window.geometry('600x300')
window.configure(background='white')
window.resizable(width=False, height=False)

# loading logo
logo = PhotoImage(file='imgs/icon_sun.png')

# widgets
LeftFrame = Frame(window, width=200, height=300, bg='MIDNIGHTBLUE', relief='raise')
LeftFrame.pack(side=LEFT)

RightFrame = Frame(window, width=395, height=300, bg='MIDNIGHTBLUE', relief='raise')
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg='MIDNIGHTBLUE')
LogoLabel.place(x=0, y=10)

# creating user
UserLabel = Label(RightFrame, text='Username: ', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='white')
UserLabel.place(x=5, y=100)

UserEntry = Entry(RightFrame, width=30)
UserEntry.place(x=175, y=115)

# creating password
PasswordLabel = Label(RightFrame, text='Password: ', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='white')
PasswordLabel.place(x=5, y=100)

PasswordEntry = Entry(RightFrame, width=30)
PasswordEntry.place(x=175, y=115)

window.mainloop()