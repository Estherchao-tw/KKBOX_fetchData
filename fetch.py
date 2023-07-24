import mysql.connector
from mysql.connector import errorcode

db_setting = {
  'user':'root', 
  'password':'888888',
  'host':'127.0.0.1',
  'database':'kkbox',
  'raise_on_warnings':True
}

conn = mysql.connector.connect(**db_setting)

#建立cursor object
with conn.cursor() as cursor:
    #查詢資料sql
    command = "SELECT * FROM charts"
    #execute
    cursor.execute(command)

    result = cursor.fetchall()
    print(result)