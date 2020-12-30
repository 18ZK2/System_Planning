import sqlite3 

#データベースの場所の指定
conn = sqlite3.connect(r'D:\virtual\venv4\myproject\db.sqlite3')
c = conn.cursor()
c.execute("select *from accounts_authuser")
list1 = c.fetchone()

print (list1[4])

conn.close()