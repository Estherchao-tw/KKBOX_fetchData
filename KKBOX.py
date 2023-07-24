from bs4 import BeautifulSoup
import requests
import json
import time
import csv
url = "https://kma.kkbox.com/charts/api/v1/daily?category=390&date=2023-07-18&lang=tc&limit=50&terr=tw&type=newrelease"
response = requests.get(url)

data = json.loads(response.text) ##JSON 轉 python
# print(data)

songlist = data['data']['charts']['newrelease']

with open('songs-utf-8-sig.csv', 'w', newline='', encoding="UTF-8-sig")as csvfile:
    #create csv.write
    write = csv.writer(csvfile)
    write.writerow(["排名","歌名","連結","作者","發行日期"])
    #write the first row
    for song in songlist:
        song_rank = song['rankings']['this_period']
        song_name = song['song_name']
        song_url = song['song_url']
        song_artist = song['artist_name']

        song_timestamp = int(song["release_date"])

        song_date = time.strftime(
            "%Y-%m-%d",time.localtime(song_timestamp)
        )

        # print("排名",song_rank)
        # print("歌名",song_name)
        # print("連結",song_url)
        # print("作者",song_artist)
        # print("發行日期",song_date)


        #透過ajas爬蟲得到的結果寫入
        write.writerow(
            [song_rank, song_name, song_url,  song_artist , song_date])


    # # 從歌曲連結取得歌詞
    # song_response = requests.get(song_url)
    # soup = BeautifulSoup(song_response.text,"html.parser")
    # lyric = soup.find('div',{'class':"lyrics"}).text
    # print("歌詞:", lyric)
  
print("-" * 30)



  