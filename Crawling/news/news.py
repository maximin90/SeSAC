import requests
from bs4 import BeautifulSoup

# def print_news(viewday): # viewday를 넣어서 만들기 
     

viewday = '20230829'
url = 'https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=001&listType=summary&date='+ viewday
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
r = requests.get(url, headers = {'User-Agent': agent})

print(r)
print(type(viewday))

if '20230801' <= viewday <= '20230831': # for문 돌려서 20230801~20230831의 기사 가져오기 
     print(r)