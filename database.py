import json
import sqlite3

conn = sqlite3.connect('user.sqlite')

conn.execute('''
    create table user (
    id INTEGER PRIMARY KEY,
    account VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
    )''')

conn.execute('''
    create table favorite (
    id INTEGER PRIMARY KEY,
    train VARCHAR(255) NOT NULL,
    user_id int NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (id)
    )''')

conn.execute('''
    create table train (
    id INTEGER PRIMARY KEY,
    trainid VARCHAR(255) NOT NULL,
    trainstation VARCHAR(255) NOT NULL
    )''')

input_file = open ('./static/json/station location.json',"r",encoding="utf-8")
json_array = json.load(input_file)

for item in json_array:
    trainid = item['StationID']
    trainstation = item['StationName']['Zh_tw']
    print (trainid)
    print (trainstation)
    sql = "insert into train (trainid, trainstation) values(?, ?)"
    values = [trainid, trainstation]
    conn.execute(sql, values)
result = conn.execute("select * from user")


for row in result:
    print("{}, {}, {}, {}".format(row[0], row[1], row[2]))
conn.commit()