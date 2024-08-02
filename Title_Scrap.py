import requests as rq

from bs4 import BeautifulSoup

from bs4 import NavigableString

qUrl = 'https://books.toscrape.com/'

qHeader = {
'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

qResp = rq.get(url=qUrl, headers= qHeader)

bSoup = BeautifulSoup(qResp.content, 'html.parser')

def removeNaviString(value):
    return list(filter(lambda x : type(x) != NavigableString , value))

olChilds = removeNaviString(bSoup.ol.children)
# print(olChilds[0].h3.getText())


titles = [ol.h3.getText() for ol in olChilds]

print(titles[4:8])