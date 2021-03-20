# import library
from tkinter import *
from tkinter import messagebox

# create window
window = Tk()
window.title('My System - Access Panel')
window.geometry('600x300')
window.configure(background='white')
window.resizable(width=False, height=False)

# loading logo
logo = PhotoImage(file='imgs/icon_sun.jpg')

# widgets
LeftFrame = Frame(window, width=200, height=300, bg='MIDNIGHTBLUE', relief='raise')
LeftFrame.pack(side=LEFT)

RightFrame = Frame(window, width=395, height=300, bg='MIDNIGHTBLUE', relief='raise')
RightFrame.pack(side=RIGHT)

window.mainloop()