
import sys
sys.path.append('..')
from myproject.settings import DATABASES
import sqlite3
from django.contrib import admin

tableNames = [
    ('django_migrations',), ('sqlite_sequence',), ('django_content_type',),
   ('auth_group_permissions',), ('auth_permission',), ('auth_group',),
  ('accounts_authuser',), ('accounts_authuser_groups',), ('accounts_authuser_user_permissions',),
 ('accounts_employeestate',), ('django_admin_log',), ('django_session',)
 ]
def ConnectServer():
    dbPath = DATABASES['default']['NAME']
    connection = sqlite3.connect(dbPath)
    cursor = connection.cursor()
    return cursor

#select name from sqlite_master where type='table';
def NameSearch(name):
    cursor = ConnectServer()
    exeCode = 'select *from '+tableNames[6][0]+' where userID = '+"'"+name+"'"
    cursor.execute(exeCode)
    result = cursor.fetchall()
    cursor.close()
    return result

