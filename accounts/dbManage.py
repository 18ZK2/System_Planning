import sqlite3 as sq
from django.contrib import admin

dbName = "..\db.sqlite3"
connection = sq.connect(dbName)
cursor = connection.cursor()
#cursor.execute('select * from accounts_authuser')
#print(cursor.fetchall())
cursor.execute("select name from sqlite_master where type='table'")
tableNames = cursor.fetchall()
for n in tableNames:
    print(n)

for n in tableNames:
    exeCode = 'select * from '+n[0]
    cursor.execute(exeCode)
    print(cursor.fetchall())
