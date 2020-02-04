import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190424',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')


#순위, 곡제목, 가수 가져오기
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number 순위
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis 곡제목
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis 아티스트


charts = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

rank = 1

for chart in charts :
    title = chart.select_one('a.title.ellipsis')
    artist = chart.select_one('a.artist.ellipsis')

    if rank is not None :

        doc = {
            'rank' : rank,
            'title' : title.text,
            'artist' : artist.text
        }
        db.genie.insert_one(doc)

        rank+=1
