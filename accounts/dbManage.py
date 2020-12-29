import sqlite3 as sq
from django.contrib import admin

dbName = "db.sqlite3"
connection = sq.connect(dbName)
cursor = connection.cursor()
cursor.execute('select * from accounts_authuser')
print(cursor)