import os
import sqlite3

# create directory
# if not os.path.exists('PythonDB'):
#     os.mkdir('PythonDB')
# os.chdir('PythonDB')

# connect to database
conn = sqlite3.connect('Sample.db', isolation_level=None)
conn.execute('DROP TABLE IF EXISTS Sales')
conn.execute('CREATE TABLE Sales (date VARCHAR(10), code VARCHAR(5), quantity INTEGER)')

# add staffs
sales = [
    ('2020/12/15', '20023', 15),
    ('2020/11/25', '42102', 28),
    ('2020/2/15', '52300', 14),
    ('2019/10/03', '31010', 21),
]
conn.executemany('INSERT INTO Sales VALUES (?, ?, ?)', sales)

# retrieve data
c = conn.cursor()

c.execute('SELECT * FROM Fruit')
for row in c:
    print(row)

c.execute('SELECT * FROM Sales')
for row in c:
    print(row)

# close database
conn.close()
