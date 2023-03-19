from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *
from utils.globalStorage import globalStorage


def getResponse(event, allDialogs=None):
    config = getConfig()
    announces = globalStorage['news_announces']
    buttonsResponse = []
    if len(announces) <= 0:
        config['message'] += 'К сожалению, анонсов сейчас нет =('
        config['tts'] += 'К сожалению, анонсов сейчас нет'
    else:
        for i in announces:
            config['message'] += f"""
            {i['text']}.\n
            {i['date']}.\n
            ------------\n
            """
            buttonsResponse.append({'title': i['text'], 'url': i['link']})
            config['tts'] += f'Вы направились в категорию "Анонсы". {i["text"]} будет {i["date"]} '

        config['buttons'] = buttonsResponse + config['buttons']
    return createResponse(event, config)


def isTriggered(event):
    token = {"аннонс", "анонс", "анонсы"}
    return isSimilarTokens(event, token) and isInLastContext(event, 'news')


announces = {'getResponse': getResponse, 'isTriggered': isTriggered}
