#每周華語新歌的曲目
import requests
import json 
import time
import mysql.connector

def get_song_data():
    
  url = "https://kma.kkbox.com/charts/api/v1/weekly?category=297&date=2023-07-20&lang=tc&limit=50&terr=tw&type=newrelease"

  response = requests.get(url)
  data = json.loads(response.text)
  # print(data)

  songlist = data["data"]["charts"]["newrelease"]
  
  return songlist

# song_data()

db_setting = {
  'user':'root', 
  'password':'Emphasize234', #請重新輸入密碼
  'host':'127.0.0.1',
  'database':'kkbox',
  'raise_on_warnings':True
}

# #建立物件連結
conn = mysql.connector.connect(**db_setting)

#建立cursor object
with conn.cursor() as cursor:
  # 資料表相關操作
  # 新增資料sql語法
  command = 'INSERT INTO charts(songID,songName,singer,releaseDate) VALUE (%s,%s,%s,%s)'
  # 取得華語單曲周榜
  songlist = get_song_data()
  
  for song in songlist:
    song_rank = song['rankings']['this_period']
    song_name = song['song_name']
    song_artist = song['artist_name']

    song_timestamp = int(song["release_date"])
    song_date = time.strftime(
        "%Y-%m-%d",time.localtime(song_timestamp)
        )
    cursor.execute(
        command,(song_rank,song_name,song_artist,song_date))

  conn.commit()
   

