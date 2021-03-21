import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-IDRT323Q\SQLEXPRESS;'
                      'Database=MySystemDB;'
                      'Trusted_Connection=yes;') 

cursor = conn.cursor()

cursor.execute('USE MySystemDB SELECT * FROM person;')

while cursor.nextset():
    try:
        results = cursor.fetchall()
        for i in range(0, len(results)):
            print(results)
            break
    except pyodbc.ProgrammingError:
        continue

'''
# insert query
count = cursor.execute("""
INSERT INTO MySystemDB.person () 
VALUES (?,?,?,?,?)""",
'SQL Server Express New 20', 'SQLEXPRESS New 20', 0, 0, CURRENT_TIMESTAMP).rowcount
conn.commit()
print('Rows inserted: ' + str(count))
'''

