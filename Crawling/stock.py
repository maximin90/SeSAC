import requests 
from bs4 import BeautifulSoup

# url = 'https://finance.naver.com/item/sise.nhn?code=005930'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

url = 'https://finance.naver.com//item/sise_day.naver?code=005930'
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
response = requests.get(url, headers = {'User-Agent': agent})
_soap = BeautifulSoup(response.text, 'lxml')
response.status_code