import multiprocessing as mp
import time
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

baseUrl = 'https://morvanzhou.github.io/'


unseen = set([baseUrl, ])
seen = set()

count, startTime = 1, time.time()


def crawl(url):
    return urlopen(url).read().decode('utf-8')


def getUrl(html):
    soup = BeautifulSoup(html, features='lxml')

    pageLinks = soup.find_all('a', {'href': re.compile('^/.*/$')})
    pageLinks = set([baseUrl + link['href'] for link in pageLinks])

    title = soup.find('meta', {'property': 'og:title'})['content']
    url = soup.find('meta', {'property': 'og:url'})['content']

    return pageLinks, title, url


if __name__ == '__main__':
    while len(unseen) != 0:
        if(len(seen) > 100):
            break
        
        pool = mp.Pool(4)

        crawlJobs = [pool.apply_async(crawl, args=(url,)) for url in unseen]
        htmls = [j.get() for j in crawlJobs]

        parseJobs = [pool.apply_async(getUrl, args=(html,)) for html in htmls]
        results = [j.get() for j in parseJobs]

        seen.update(unseen)
        unseen.clear()

        for pageLinks, title, url in results:
            print(count, title, ':', url)

            count += 1
            unseen.update(pageLinks - seen)

    print('\nTotal time spent: %.2f s' % (time.time() - startTime))