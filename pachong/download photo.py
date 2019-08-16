
from bs4 import BeautifulSoup
import requests
import os


URL = "https://www.7160.com/"


html = requests.get(URL).text
soup = BeautifulSoup(html, 'lxml')
img_ul = soup.find_all('div', {"class": "gd1"})

os.makedirs('./img1/', exist_ok=True)

for ul in img_ul:
    imgs = ul.find_all('img')
    print(imgs)
    for img in imgs:
        url = img['src']
        print(url)
        r = requests.get(url, stream=True)
        image_name = url.split('/')[-1]
        with open('./img/%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' % image_name)