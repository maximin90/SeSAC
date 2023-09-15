import time
from datetime import datetime

def get_oil_price(code):
    delay = 0.01
    page = 1
    result = []
    start_date = '2018.02.01'
    end_date = '2020.05.18'
    start_time = datetime.now()
    
    # 수집
    print('[{}] 데이터 수집을 시작합니다. (code: {})'.format(start_time.strftime('%Y/%m/%d %H:%M:%S'), code))
    while(True):
        url = 'https://finance.naver.com/marketindex/worldDailyQuote.nhn?marketindexCd={}&fdtc=2&page={}'.format(code, page)
        data = pd.read_html(url)[0].dropna()
        if page != 1:
            try:
                if start_date in data.iloc[:,0].values:
                    data = data.loc[:data.iloc[:,0].values.tolist().index(start_date),]
                    result.append(data)
                    break
            except:
                break
        result.append(data)
        page += 1
        time.sleep(delay)
    
    # 가공
    oil_price = pd.concat(result).reset_index(drop=True)
    oil_price.columns = ['date', 'price', '전일대비', '등락율']
    oil_price = oil_price.loc[oil_price['date'].tolist().index(end_date):,]
    oil_price['date'] = oil_price['date'].apply(lambda x: datetime.strptime(x, '%Y.%m.%d'))
    oil_price = oil_price[['date', 'price']]
    oil_price.insert(0, 'code', code)
    oil_price = oil_price[::-1].reset_index(drop=True)
    
    end_time = datetime.now()
    print('[{}] 데이터 수집을 종료합니다. (code: {}, 수집시간: {}초, 데이터수: {:,}개)'.format(end_time.strftime('%Y/%m/%d %H:%M:%S'), code, (end_time-start_time).seconds, len(oil_price)))
    return oil_price
    
oil_price_du = get_oil_price('OIL_DU')
oil_price_wti = get_oil_price('OIL_CL')
oil_price_brent = get_oil_price('OIL_BRT')