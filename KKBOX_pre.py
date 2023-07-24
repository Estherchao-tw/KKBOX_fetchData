from bs4 import BeautifulSoup
import requests

url = "https://kma.kkbox.com/charts/daily/newrelease?cate=390&lang=tc&terr=tw#"
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")
print(soup.prettify())

## newrelease on the web, which is in f12>Network>newrelease,is like url of web.it shows nothing at preview,and it just an empty shell,so it cannot fetch data from the server 
## where is the data?
# http is designed to transfer information between networked devices and provides a framework for client/server communication.
#http request contains the HTTP method (mostly get),target url, http request headers,and additional url parameters.
# http response includes information on the request's status (200),the requested content (html,JSON,image...) and optional http headers on how to interpret this content.

AJAX 爬蟲
kkbox give us an empty shell of html framework,and they fill data by js.

#要在json找到傳遞資料的api
# choose fetch and xhr, you will find the api easily.
daily?category=.... >preview 
裡面有我們要抓的資料(歌手、歌名、日期等等)