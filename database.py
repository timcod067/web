import sqlite3

conn = sqlite3.connect('user.sqlite')

conn.execute('''
    create table user (
    id INTEGER PRIMARY KEY,
    account VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
    )''')

result = conn.execute("select * from user")
for row in result:
    print("{}, {}, {}, {}".format(row[0], row[1], row[2]))
conn.commit()