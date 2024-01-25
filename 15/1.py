import os
import sqlite3

# create directory
os.mkdir('PythonDB')
os.chdir('PythonDB')

# connect to database
conn = sqlite3.connect('Cosmos.db', isolation_level=None)
sql = '''
CREATE TABLE Member (id VARCHAR(4), name VARCHAR(20), age INTEGER, email VARCHAR(128))
'''
conn.execute(sql)

# add data
conn.execute('''
    INSERT INTO Member VALUES ('1018', 'Kenta', 23, 'ken@py.co.ja'), ('1019', 'Ryosei', 19, 'ryosei@gmail.com')
''')

# retrieve data
c = conn.cursor()
c.execute("SELECT * FROM Member")

# print data
for row in c:
    print(row)

# close database
conn.close()
