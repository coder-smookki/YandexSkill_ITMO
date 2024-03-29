from ..utils.textNormalizer.index import textNormalizer
import requests
from bs4 import BeautifulSoup as bs

def contests(query, lang):
    result = []

    if lang == 'en-US':
        parserLink = 'https://news.itmo.ru/en/events/'
    else:
        parserLink = 'https://news.itmo.ru/ru/events/'

    try:
        r = requests.get(parserLink)
    except:
        return False

    soup = bs(r.text, "html.parser")
    posts = soup.select('div[data-block-id=contests]>div>ul>li')
    for post in posts:
        a = post.select('h4>a')
        text = a[0].getText()
        link = 'https://news.itmo.ru' + a[0].get('href')
        date = post.select('.information>span')[0].getText()
        result.append({
            'text': textNormalizer(text),
            'link': textNormalizer(link),
            'date': textNormalizer(date)
        })

    return result
