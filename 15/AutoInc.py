import os
import sqlite3

# create directory
if not os.path.exists('PythonDB'):
    os.mkdir('PythonDB')
os.chdir('PythonDB')

# connect to database
conn = sqlite3.connect('auto.db', isolation_level=None)
conn.execute('DROP TABLE IF EXISTS Member')
conn.execute('CREATE TABLE Member (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(20), age INTEGER, email VARCHAR(128))')

# add data
conn.execute('''
    INSERT INTO Member VALUES (0, 'Kenta', 23, 'ken@py.co.ja'), (3, 'Ryosei', 19, 'ryosei@gmail.com')
''')
conn.execute('''
    INSERT INTO Member (name, age, email) VALUES ('Taro', 19, 'taro@email.com'), ('Hanako', 21, 'hanako@email.com')
''')

# retrieve data
c = conn.cursor()
c.execute("SELECT * FROM Member")

# print data
for row in c:
    print(row)

# close database
conn.close()
