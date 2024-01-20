import requests
from bs4 import BeautifulSoup

url = 'https://www.formula1.com/en/results.html/2023/team.html'

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')
table = soup.find('table', class_='resultsarchive-table')


if table:
    for row in table.find_all('tr'):
        data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
        
        print(data)
else:
    print('table not found')
