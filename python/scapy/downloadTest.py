from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re

# Open the web page
html = urlopen('https://movie.douban.com/subject/30331149/all_photos').read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')

# Get the image url
imgURL = soup.find_all('img', {'src': re.compile('https://.*/view/.*jpg')})
imgURL = [img['src'] for img in imgURL]
print(imgURL)

for img in imgURL:
    r = requests.get(img, stream=True)
    imageName = img.split('/')[-1]
    print('call img')

    with open('/home/mike/python/scapy/pic/%s' % imageName, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)
        print('call open')
    print('Saved %s' % imageName)