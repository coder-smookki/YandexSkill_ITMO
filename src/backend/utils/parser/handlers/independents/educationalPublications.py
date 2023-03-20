import requests
from bs4 import BeautifulSoup as bs
from ..utils.textNormalizer.index import textNormalizer


def educationalPublications(query):
    if not query:
        raise TypeError('Empty query is not allowed')
    result = []
    body = {"searchTextBox": query}
    try:
        r = requests.post('http://books.ifmo.ru/search_form/search.htm', data=body)
    except:
        return False
    soup = bs(r.text, "html.parser")
    posts = soup.select('.contentIndents table:nth-child(n+3) td', limit=3)
    for post in posts:
        title = post.select('h4')[0].getText()
        textArr = post.findAll(text=True, recursive=False)
        text = textNormalizer(textArr[0]) + post.select('span')[0].getText() + textNormalizer(textArr[1])
        link = 'http://books.ifmo.ru' + post.select('p a')[0].get('href')
        result.append({
            'title': textNormalizer(title),
            'text': textNormalizer(text),
            'link': textNormalizer(link)
        })
    return result
