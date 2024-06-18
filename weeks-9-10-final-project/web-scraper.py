import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://nuforc.org/subndx/?id=all'

# page = urlopen(url)

# html = page.read().decode('utf-8')

# table_start = html.find('<tbody>')
# table_end = html.find('</tbody>')

# print(html[table_start: table_end])

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

headers = soup.find('thead')

table_body = soup.find('tbody')

stuff = table_body.find_all('tr')
print(stuff)
