import requests
from bs4 import BeautifulSoup
import datetime

def print_stock_price(code, page_num):
    result = [[], [], [], [], [], [], []]

    for n in range(page_num):
        url = 'https://finance.naver.com/item/sise_day.nhn?code='+code+'&page='+str(n+1)
        agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        r = requests.get(url, headers = {'User-Agent': agent})
        html = r.content
        soup = BeautifulSoup(html, 'html.parser')
        tr = soup.select('table > tr')

        for i in range(1, len(tr)-1):
            if tr[i].select('td')[0].text.strip():
                result[0].append(tr[i].select('td')[0].text.strip())
                result[1].append(tr[i].select('td')[1].text.strip())
                result[2].append(tr[i].select('td')[2].text.strip())
                result[3].append(tr[i].select('td')[3].text.strip())
                result[4].append(tr[i].select('td')[4].text.strip())
                result[5].append(tr[i].select('td')[5].text.strip())
                result[6].append(tr[i].select('td')[6].text.strip())

    for i in range(len(result[0])):
        if  '2023.08.01' <= result[0][i]  <= '2023.08.31':
            print(result[0][i], result[1][i], result[2][i],result[3][i],result[4][i],result[5][i],result[6][i])



stock_code = '005930'
pages = 4

print_stock_price(stock_code, pages)
