
import sys
sys.path.append('..')

import sqlite3
from django.contrib import admin
from myproject.settings import DATABASES


#select name from sqlite_master where type='table';
tableNames = [
    ('django_migrations',), ('sqlite_sequence',), ('django_content_type',),
   ('auth_group_permissions',), ('auth_permission',), ('auth_group',),
  ('accounts_employeestate',), ('accounts_authuser',), ('accounts_authuser_groups',),
 ('accounts_authuser_user_permissions',), ('django_admin_log',), ('django_session',),
('accounts_roomcheck',)]

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
def StateSearch(name):
 
    state ='ユーザーIDが存在しませんでした'
    if name!=None:
        exeCode = 'select *from '+tableNames[6][0]+' where userID = '+"'"+name+"'"
        result = Execute(exeCode)
        if result!=[]:
            state = empStateDic[result[0][1]]
    return state
#ユーザーIDで部屋の場所を検索
def PlaceSearch(placeNum):
  
    places ='指定した場所に出勤した人はいませんでした'
    if placeNum!=None:
        exeCode = 'select userID from '+tableNames[12][0]+' where RoomID = '+str(placeNum)
        print(exeCode)
        result = Execute(exeCode)
        if result!=[]:
            places = result
    return places
#テーブル名取得    
def TableInfo(num):

    exeCode = 'PRAGMA table_info('+tableNames[num][0]+')'
    return Execute(exeCode)