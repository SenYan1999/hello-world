import os
import re
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

# define some global variables
baseURL = 'http://kuerby.com'

SubHtml = urlopen('http://kuerby.com/art-type-id-1-pg-1.html').read().decode()
SubSoup = BeautifulSoup(SubHtml, features='lxml')

SubPages = SubSoup.find_all('a', {'target': '_blank', 'title': re.compile('.*')})
SubURLs = [baseURL + u['href'] for u in SubPages]

for url in SubURLs:

    currentURL = url         
    html = urlopen(currentURL).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    
    # make a pic directory
    title = soup.find_all('div', {'class': 'page_title'})[0].get_text()
    myPath = '/home/mike/python/scapy/%s' % title
    os.mkdir(myPath)
    
    while(currentURL):
        html = urlopen(currentURL).read().decode('utf-8')
        soup = BeautifulSoup(html, features='lxml')

        lables = soup.find_all('a', {'class', 'pagelink_a'})
        imgURL = [img['src'] for img in soup.find_all('img')]

        # download images
        for img in imgURL:
            URL = baseURL + '/' + img
            imageName = img.split('/')[-1]
            r = requests.get(URL, stream=True)

            picPath = myPath + '/' + imageName

            with open(picPath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    f.write(chunk)
            print('Saved %s' % imageName)

        # judge if there is next page
        for lab in lables:
            if(lab.get_text() == '下一页'):
                currentURL = baseURL + lab['href']
                break
            else:
                currentURL = None