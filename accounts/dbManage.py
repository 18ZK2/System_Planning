import sqlite3
from django.contrib import admin

tableNames = [('django_migrations',), ('sqlite_sequence',), ('django_content_type',), ('auth_group_permissions',), ('auth_permission',), ('auth_group',), ('accounts_authuser',), ('accounts_authuser_groups',), ('accounts_authuser_user_permissions',), ('accounts_employeestate',), ('django_admin_log',), ('django_session',)]
#select name from sqlite_master where type='table';

def NameSearch(name):
    print(name)
    dbPath = "..\db.sqlite3"
    connection = sqlite3.connect(dbPath)
    print(connection)
    cursor = connection.cursor()
    print(cursor)
    exeCode = 'select userID from '+tableNames[6][0]
    cursor.execute(exeCode)
    return cursor.fetchall()
