from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *
from utils.globalStorage import globalStorage


def getResponse(event, allDialogs=None):
    config = getConfig()
    announces = globalStorage['news_announces']
    buttonsResponse = []
<<<<<<< HEAD
    if len(announces) <= 0:
        config['message'] += 'К сожалению, анонсов сейчас нет =('
        config['tts'] += 'К сожалению, анонсов сейчас нет'
=======
    if len(announces) == 0:
        config['message'] = "Новый новостей на данный момент нет."
        config['tts'] = "Новый новостей на данный момент нет"
>>>>>>> 89a0f4675af16e98a0b66d8019b2a42f4b4b7da0
    else:
        for i in announces:
            config['message'] += f"""
            {i['text']}.\n
            {i['date']}.\n
            ------------\n
            """
<<<<<<< HEAD
            buttonsResponse.append({'title': i['text'], 'url': i['link']})
=======
            buttonsResponse.append({'title': i['text'], 'url': i['link'], 'hide': False})
>>>>>>> 89a0f4675af16e98a0b66d8019b2a42f4b4b7da0
            config['tts'] += f'Вы направились в категорию "Анонсы". {i["text"]} будет {i["date"]} '

        config['buttons'] = buttonsResponse + config['buttons']
    return createResponse(event, config)


def isTriggered(event):
    token = {"аннонс", "анонс", "анонсы"}
    return isSimilarTokens(event, token) and isInLastContext(event, 'news')


announces = {'getResponse': getResponse, 'isTriggered': isTriggered}
