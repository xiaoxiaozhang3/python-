# 需安装requests模块
import requests
# import webbrowser

#在百度上查找 "xiaoxiaozhang"
param = {"wd": "xiaoxiaozhang"}
r = requests.get('http://www.baidu.com/s', params=param)
#返回查找到的网页
print(r.url)
# webbrowser.open(r.url)

# post请求 模拟登录一个网页http://pythonscraping.com/pages/files/processing.php
# 返回 hello，there，xiaoxiao zhang
data = {'firstname': 'xiaoxiao', 'lastname': 'zhang'}
r = requests.post('http://pythonscraping.com/pages/files/processing.php', data=data)
print(r.text)

#上传图片
file = {'uploadFile': open('./image.png', 'rb')}
r = requests.post('http://pythonscraping.com/files/processing2.php', files=file)
print(r.text)

#登录之后再次模拟登录
payload = {'username': 'xiaoxiao', 'password': 'password'}
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())
r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
print(r.text)



session = requests.Session()
payload = {'username': 'xiaoxiao', 'password': 'password'}
r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())
r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(r.text)