import requests
from bs4 import BeautifulSoup as bs
import re
from ...utils.textNormalizer.index import textNormalizer


def getAllGroups(args):
    if not isinstance(args, list):
        raise TypeError(
            'The argument to the findGroups must be an array: [degree(int), course(int)].')
    # 3 - бакалавриат
    # 4 - магистратура
    # 5 - специалитет
    degree = args[0]

    if degree < 3 or degree > 5:
        raise TypeError('''Degree must be:
            3 - undergraduate (бакалавриат) 
            4 - magistracy (магистратура)
            5 - specialty (специалитет)''')

    # курс
    course = args[1]

    result = {
        'totalFounded': 0,
        'groups': []
    }
    body = {"degree": degree, "course": course}
    try:
        r = requests.post(
            'https://student.itmo.ru/ru/timetable/list/', data=body)
    except:
        return False

    soup = bs(r.text, "html.parser")
    pageContent = soup.select_one('.wrapper > div > div')

    totalFounded = int(
        pageContent
        .select_one('.timetable-cards__result-heading > .timetable-cards__result-count')
        .getText()
    )
    result['totalFounded'] = totalFounded

    groupList = pageContent.select('section')
    for group in groupList:
        groupResult = _fillGroups(group)

        result['groups'].append(groupResult)

    return result


def _fillGroups(groupTag):
    groupResult = {
        'mask': '',
        'list': []
    }

    maskTag = groupTag.select_one('.timetable-cards__group-number > span')

    # transform tags to normal string
    regex = re.compile(r'<span>(.*?)<\/span>', re.DOTALL)
    match = regex.search(str(maskTag))
    if match:
        span_text = match.group(1)
        mask = textNormalizer(
            re.sub(r'<i><\/i>', 'x', span_text)).replace(' ', '')
    # ----
    groupResult['mask'] = mask

    groupList = groupTag.select('.timetable-cards__group-list-item > a')

    for group in groupList:
        groupName = textNormalizer(group.getText())
        groupResult['list'].append(groupName)
    return groupResult
