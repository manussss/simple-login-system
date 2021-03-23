import pyodbc
from tkinter import messagebox
from tkinter.messagebox import showerror

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-IDRT323Q\SQLEXPRESS;'
                      'Database=MySystemDB;'
                      'Trusted_Connection=yes;'
                      'autocommit=True;') 

cursor = conn.cursor()

def select():
    cursor.execute('USE MySystemDB SELECT * FROM person;')

    while cursor.nextset():
        try:
            results = cursor.fetchall()
            for i in range(0, len(results)):
                print(results)
                break
        except pyodbc.ProgrammingError:
            continue


def insert(name, your_email, your_username, your_password):
    firstName = name
    email = your_email
    username = your_username
    password = your_password
    if (firstName == '' and email == '' and username == '' and password == ''):
        messagebox.showerror(title='Register Error', message='Fill all the fields.')
    else:
        cursor.execute("USE MySystemDB INSERT INTO person (firstName, email, username, pass) VALUES (?,?,?,?);", (firstName, email, username, password))
        cursor.commit()
        
        messagebox.showinfo(title='Register Info', message='Account Created')
    
def check_login(your_user, your_password):
    username = your_user
    password = your_password
    cursor.execute('USE MySystemDB SELECT username, pass FROM person WHERE username = ? AND pass = ?', 
                   (username, password))
    verify_login = cursor.fetchone()
    print(verify_login)
    try:
        if (username in verify_login and password in verify_login):
            messagebox.showinfo(title='Login Info', message='Confirmed Access')
    except:
        messagebox.showinfo(title='Login Info', message='Access Denied')
    


