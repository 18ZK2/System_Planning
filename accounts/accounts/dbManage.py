
import sys
sys.path.append('..')

import sqlite3
from django.contrib import admin
from myproject.settings import DATABASES


#select name from sqlite_master where type='table';
tableNames = [
    ('django_migrations',), ('sqlite_sequence',), ('django_content_type',),
   ('auth_group_permissions',), ('auth_permission',), ('auth_group',),
  ('accounts_authuser',), ('accounts_authuser_groups',), ('accounts_authuser_user_permissions',),
 ('accounts_employeestate',), ('django_admin_log',), ('django_session',)
 ]

empStateDic = {0:'入力なし',1:'出勤',2:'社用外出',3:'私用外出',4:'遅刻',5:'早退',6:'休み',7:'午前休',8:'午後休',9:'テレワーク',10:'退社',11:'出張'}    

#データベースに接続しexeCodeを実行
def Execute(exeCode):
    dbPath = DATABASES['default']['NAME']
    connection = sqlite3.connect(dbPath)
    cursor = connection.cursor()
    cursor.execute(exeCode)
    result = cursor.fetchall()
    cursor.close()
    return result
#ユーザーIDでaccounts_employeestateのEMPstateを取得
def NameSearch(name):

    exeCode = 'select *from '+tableNames[9][0]+' where userID = '+"'"+name+"'"
    result = Execute(exeCode)
    state ='ユーザーIDが存在しませんでした'
    if result!=[]:
       state = empStateDic[result[0][1]]
    return state
#テーブル名取得    
def TableInfo(num):

    exeCode = 'PRAGMA table_info('+tableNames[num][0]+')'
    return Execute(exeCode)