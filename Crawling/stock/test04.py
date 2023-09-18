import requests
from bs4 import BeautifulSoup

# Define the URL for the first page
base_url = 'https://finance.naver.com/item/sise_day.naver?code=005930&page=1'

# Define the desired date range
start_date = '2023-09-01'
end_date = '2023-09-15'

# Function to format date from 'YYYY.MM.DD' to 'YYYY-MM-DD'
def format_date(date):
    parts = date.split('.')
    return f'{parts[0]}-{parts[1]}-{parts[2]}'

# Function to scrape data from a single page
def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='type2')

    data = []

    for row in table.find_all('tr')[1:]:
        columns = row.find_all('td')
        if len(columns) == 7:
            date = format_date(columns[0].get_text().strip())
            closing_price = columns[1].get_text().strip()

            if start_date <= date <= end_date:
                data.append(f'Date: {date}, Closing Price: {closing_price}')
    
    return data

# Function to get the total number of pages
def get_total_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    page_nav = soup.find('td', class_='pgRR')
    
    if page_nav:
        last_page_url = page_nav.a['href']
        total_pages = int(last_page_url.split('=')[-1])
        return total_pages
    else:
        return 1

# Main scraping logic
total_pages = get_total_pages(base_url)
all_data = []

for page in range(1, total_pages + 1):
    page_url = f'{base_url}&page={page}'
    page_data = scrape_page(page_url)
    all_data.extend(page_data)

# Print the scraped data
for entry in all_data:
    print(entry)
