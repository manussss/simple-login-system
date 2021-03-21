# import library
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database

# change to register screen
def register():
    login_button.place(x=5000)
    register_button.place(x=5000)
    
    name_label = Label(right_frame, text='Name: ', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='white')
    name_label.place(x=5, y=5)
    
    name_entry = ttk.Entry(right_frame, width=39)
    name_entry.place(x=115, y=20)
    
    email_label = Label(right_frame, text='Email: ', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='white')
    email_label.place(x=5, y=55)
    
    email_entry = ttk.Entry(right_frame, width=41)
    email_entry.place(x=100, y=68)
    
    window_register_button = ttk.Button(right_frame, text='Register', width=25)
    window_register_button.place(x=95, y=220)
    
    def back_to_login():
        name_label.place(x=5000)
        name_entry.place(x=5000)
        email_label.place(x=5000)
        email_entry.place(x=5000)
        window_register_button.place(x=5000)
        back.place(x=5000)
        
        login_button.place(x=95, y=220)
        register_button.place(x=95, y=260)
        
    back = ttk.Button(right_frame, text='back', width=20, command=back_to_login)
    back.place(x=111, y=260)
    

# create window
window = Tk()
window.title('My System - Access Panel')
window.geometry('600x300')
window.configure(background='white')
window.resizable(width=False, height=False)

# loading logo
logo = PhotoImage(file='imgs/icon_sun.png')

# widgets
left_frame = Frame(window, width=200, height=300, bg='MIDNIGHTBLUE', relief='raise')
left_frame.pack(side=LEFT)

right_frame = Frame(window, width=395, height=300, bg='MIDNIGHTBLUE', relief='raise')
right_frame.pack(side=RIGHT)

logo_label = Label(left_frame, image=logo, bg='MIDNIGHTBLUE')
logo_label.place(x=0, y=10)

# creating user
user_label = Label(right_frame, text='Username: ', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='white')
user_label.place(x=5, y=100)

user_entry = ttk.Entry(right_frame, width=30)
user_entry.place(x=165, y=115)

# creating password
password_label = Label(right_frame, text='Password: ', font=('Century Gothic', 20), bg='MIDNIGHTBLUE', fg='white')
password_label.place(x=5, y=150)

password_entry = ttk.Entry(right_frame, width=30, show='•')
password_entry.place(x=165, y=165)

# buttons
login_button = ttk.Button(right_frame, text='Login', width=25)
login_button.place(x=95, y=220)

register_button = ttk.Button(right_frame, text='Register', width=25, command=register)
register_button.place(x=95, y=260)

window.mainloop()