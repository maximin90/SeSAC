import requests
from bs4 import BeautifulSoup

# 크롤링할 웹 페이지 URL
url = "https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=001&listType=summary&date=20230831"

# 웹 페이지 내용을 가져옵니다.
response = requests.get(url)

# HTTP 요청이 성공한 경우에만 진행합니다.
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 기사 목록을 찾습니다.
    articles = soup.find_all('li', class_='cluster_item')
    
    # 각 기사의 본문을 크롤링합니다.
    for article in articles:
        # 기사 제목과 링크
        title = article.find('a', class_='cluster_text_headline')
        article_url = title['href']
        article_title = title.text.strip()
        
        # 기사 본문 페이지에 접속하여 본문 추출
        article_response = requests.get(article_url)
        if article_response.status_code == 200:
            article_soup = BeautifulSoup(article_response.text, 'html.parser')
            
            # 기사 본문 추출
            article_content = article_soup.find('div', class_='article_body')
            
            if article_content:
                print("기사 제목:", article_title)
                print("기사 본문:")
                print(article_content.text.strip())
                print("="*50)
else:
    print("HTTP 요청이 실패했습니다. 상태 코드:", response.status_code)