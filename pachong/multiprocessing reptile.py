import multiprocessing as mp
import time
from urllib.request import urlopen, urljoin
from bs4 import BeautifulSoup
import re


base_url = 'https://morvanzhou.github.io/'
restricted_crawl = True
#DON'T OVER CRAWL THE WEBSITE OR YOU MAY NEVER VISIT AGAIN


def crawl(url):
    response = urlopen(url)

    return response.read().decode()

def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    urls = soup.find_all('a', {"href": re.compile('^/.+?/$')})
    title = soup.find('h1').get_text().strip()
    page_urls = set([urljoin(base_url, url['href']) for url in urls])
    url = soup.find('meta', {'property': "og:url"})['content']
    return title, page_urls, url

unseen = set([base_url, ])
seen = set()

count, t1 = 1, time.time()

while len(unseen) != 0:  # still get some url to visit
    if restricted_crawl and len(seen) > 20:
        break

    print('\nDistributed Crawling...')
    htmls = [crawl(url) for url in unseen]

    print('\nDistributed Parsing...')
    results = [parse(html) for html in htmls]

    print('\nAnalysing...')
    seen.update(unseen)  # seen the crawled
    unseen.clear()  # nothing unseen

    for title, page_urls, url in results:
        print(count, title, url)
        count += 1
        unseen.update(page_urls - seen)  # get new url to crawl
print('Total time: %.1f s' % (time.time() - t1,))  # 53 s

#使用多线程的方式爬取
unseen = set([base_url,])
seen = set()

pool = mp.Pool(4)
count, t1 = 1, time.time()
while len(unseen) != 0:                 # still get some url to visit
    if restricted_crawl and len(seen) > 20:
            break
    print('\nDistributed Crawling...')
    crawl_jobs = [pool.apply_async(crawl, args=(url,)) for url in unseen]
    htmls = [j.get() for j in crawl_jobs]                                       # request connection

    print('\nDistributed Parsing...')
    parse_jobs = [pool.apply_async(parse, args=(html,)) for html in htmls]
    results = [j.get() for j in parse_jobs]                                     # parse html

    print('\nAnalysing...')
    seen.update(unseen)         # seen the crawled
    unseen.clear()              # nothing unseen

    for title, page_urls, url in results:
        print(count, title, url)
        count += 1
        unseen.update(page_urls - seen)     # get new url to crawl
print('Total time: %.1f s' % (time.time()-t1, ))    # 16 s !!!