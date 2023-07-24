import mysql.connector
from mysql.connector import errorcode

db_setting = {
  'user':'root', 
  'password':'888888', #請重新輸入密碼
  'host':'127.0.0.1',
  'database':'kkbox',
  'raise_on_warnings':True
}

try:
  #建立物件連結
  conn = mysql.connector.connect(**db_setting)
except Exception as ex:
  print(ex)
