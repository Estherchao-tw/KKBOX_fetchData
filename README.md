# KKBOX_fetchData

## Description
python爬蟲KKBOX每周榜單資料，存入mysql資料庫，並透過python 執行mysql search <br>
使用 Python 套件串接資料庫系統 mysql-connector 或 PyMySQL <br>

## Motivation and basics
學習透過python 建立mysql資料庫(demo_mysql_test.py)<br>
爬取ajax資料儲存至資料庫(KKBOX_db_py.py)<br>
從資料庫搜尋資料(fetch.py)<br>

## Installation / How to setup

### Requirement
mysql-connector-python     8.1.0<br>
requests                   2.31.0<br>


## Copy-pastable quick start code example

### scrapy by requests
  `url = "https://kma.kkbox.com/charts/api/v1/weekly?category=297&date=2023-07-20&lang=tc&limit=50&terr=tw&type=newrelease"`

  `response = requests.get(url)` <br>
  `data = json.loads(response.text)`
  
### connect to mysql
`db_setting = { `<br>
  `'user':'root', `<br>
  `'password':'8888', #請重新輸入密碼`<br>
  `'host':'127.0.0.1',`<br>
  `'database':'kkbox',`<br>
 ` 'raise_on_warnings':True`<br>
`}`<br>

`conn = mysql.connector.connect(**db_setting)`
### find data
**建立cursor object**
`with conn.cursor() as cursor:`<br>
   ` **查詢資料sql**`<br>
  `  command = "SELECT * FROM charts"`<br>
  `  **execute** `<br>
 `   cursor.execute(command)`<br>
<br>
`    result = cursor.fetchall()`<br>
`    print(result)`<br>

### demo
![img](demo.jpg)

