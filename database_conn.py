import pyodbc

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
    cursor.execute("USE MySystemDB INSERT INTO person (firstName, email, username, pass) VALUES (?,?,?,?);", (firstName, email, username, password))
    cursor.commit()


