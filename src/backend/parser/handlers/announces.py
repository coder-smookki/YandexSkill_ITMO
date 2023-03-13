from .utils.textNormalizer.index import textNormalizer
 
def announces(soup):
    result = []

    posts = soup.select('div[data-block-id=announces]>div>ul>li')
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
