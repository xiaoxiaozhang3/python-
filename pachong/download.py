import os
from urllib.request import urlretrieve
import requests

os.makedirs('./img/', exist_ok=True)

IMAGE_URL = "https://xiaoxiaozhang3.github.io/img/cart_cover.jpg"

#将IMAGE_URL 下载到/img文件夹
urlretrieve(IMAGE_URL, './img/image1.png')

#先下载好文件在内存中才能打开
r = requests.get(IMAGE_URL)
with open('./img/image2.png', 'wb') as f:
    f.write(r.content)

#一次下载32单位的图片
r = requests.get(IMAGE_URL, stream=True)    # stream loading
with open('./img/image3.png', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)

