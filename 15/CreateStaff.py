import os
import sqlite3

# create directory
if not os.path.exists('PythonDB'):
    os.mkdir('PythonDB')
os.chdir('PythonDB')

# connect to database
conn = sqlite3.connect('Shop.db', isolation_level=None)
conn.execute('CREATE TABLE Staff (name VARCHAR(20), age INTEGER, section VARCHAR(48))')

# add staffs
staffs = [
    ('高専健太', 25, '販売'),
    ('川崎洋子', 18, '販売'),
    ('花尾翔', 36, '仕入れ'),
    ('大山海男', 24, '経理'),
    ('石井洋治', 19, '販売')
]
conn.executemany('INSERT INTO Staff VALUES (?, ?, ?)', staffs)

# retrieve data
c = conn.cursor()
c.execute('SELECT * FROM Staff')

# print data
for row in c:
    print(row)

# close database
conn.close()
