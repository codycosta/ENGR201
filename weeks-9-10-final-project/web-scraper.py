
from urllib.request import urlopen

url = 'https://nuforc.org/subndx/?id=all'

page = urlopen(url)

html = page.read().decode('utf-8')

table_start = html.find('<tbody>')
table_end = html.find('</tbody>')

print(html[table_start: table_end])
