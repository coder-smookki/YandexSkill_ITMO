import requests
from bs4 import BeautifulSoup as bs
from src.parser.handlers.announces import announces
from src.parser.handlers.contests import contests
from src.parser.handlers.independents.educationalPublications import educationalPublications
from src.parser.handlers.independents.timetable.getAllGroups import getAllGroups
from src.parser.handlers.independents.timetable.getGroupTimetable import getGroupTimetable

# infoType - тип информации, которую нужно спарсить
# query - строка запроса, если используется (необязательная)

# Типы:
#  - announces - анонсы
#  - contests - конкурсы
#  - educationalPublications - учебные пособия (требуется query)
#  - timetable.getAllGroups - получить все группы по форме обучения и курсу
#  - timetable.getGroupTimetable - получить все занятия группы по имени группы и форме обучения

def parser(infoType, query=''):
    types = {
        'announces': {'url': 'https://news.itmo.ru/ru/events/', 'handler': announces},
        'contests': {'url': 'https://news.itmo.ru/ru/events/', 'handler': contests},
        'educationalPublications': {'handler': educationalPublications},
        'timetable.getAllGroups': {'handler': getAllGroups},
        'timetable.getGroupTimetable': {'handler': getGroupTimetable} 
    }

    if not infoType in types:
        raise TypeError('Unknown type')

    if not 'url' in types[infoType]:
        return types[infoType]['handler'](query)

    try:
        r = requests.get(types[infoType]['url'])
    except:
        return False

    soup = bs(r.text, "html.parser")

    return types[infoType]['handler'](soup)
