from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random

baseUrl = 'https://baike.baidu.com'
his = ['/item/bilibili/7056160?fr=aladdin']

url = baseUrl + his[-1]

for i in range(20):
    # Get the soup of some web page
    url = baseUrl + his[-1]
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')

    # Get the information needed
    head = soup.find('h1')
    print(head.get_text(), 'URL:', url)

    # Put next page into history
    links = soup.find_all('a', {'target': '_blank', 'href': re.compile('/item/(%.{2})+')})
    his.append(random.sample(links, 1)[0]['href'])