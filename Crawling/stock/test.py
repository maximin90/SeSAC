import requests
import time
import pandas as pd
 
from bs4 import BeautifulSoup as bs
from datetime import datetime
 
 
def exportData(code, startdate, enddate):
    
    isEnd = False
    res = {
        'index': [],
        'data': []
    }
    
    print("Start")
    
    page = 1
    while isEnd != True:
        url = "https://finance.naver.com/item/sise_day.nhn?code="+code+"&amp;page="+ str(page)
        response = requests.get(url)
        html = bs(response.text, 'html.parser')
        
        # parse
        trList = html.find_all("tr", {"onmouseover":"mouseOver(this)"})
        for tr in trList:
            tdList = tr.find_all('td')
#             print(tdList[0].text.strip())  # 날짜
#             print(tdList[1].text.strip())  # 종가
#             print(tdList[2].text.strip())  # 전일비
#             print(tdList[3].text.strip())  # 시가
#             print(tdList[4].text.strip())  # 고가
#             print(tdList[5].text.strip())  # 저가
#             print(tdList[6].text.strip())  # 거래량
        
            date = tdList[0].text.strip()  # 날짜
            closePrice = int(tdList[1].text.strip().replace(',', ''))  # 종가
            diffPrice = int(tdList[2].text.strip().replace(',', ''))  # 전일비
            openPrice = int(tdList[3].text.strip().replace(',', ''))  # 시가
            highPrice = int(tdList[4].text.strip().replace(',', ''))  # 고가
            lowPrice = int(tdList[5].text.strip().replace(',', ''))  # 저가
            volume = int(tdList[6].text.strip().replace(',', ''))  # 거래량
            
            target = datetime.fromisoformat(date.replace('.', '-'))
            if target < start:
                isEnd = True
                break
            elif target < end and target > start:
                print(target)
                # insert index
                res['index'].insert(0, date)
                
                # insert data with ["High","Low","Open","Close","Volume","Adj Close"]
                res['data'].insert(0, [highPrice, lowPrice, openPrice, closePrice, volume])
                        
        page += 1
        time.sleep(2)
        
    df = pd.DataFrame(data=res['data'], index=res['index'])
    df.to_json(code+'.json', orient='split', date_format='index')
    
    print("Start - Done")
    
code = "005930"
start = datetime(2019, 1, 1)
end = datetime(2019, 12, 31)
 
exportData(code, start, end)
