from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *
from utils.globalStorage import globalStorage


def getResponse(event, allDialogs=None):
    config = getConfig()
    announces = globalStorage['news_announces']
    buttonsResponse = []
    for i in announces:
        config['message'] += f"""
        {i['text']}.\n
        {i['date']}.\n
        ------------\n
        """
        buttonsResponse.append({'title': i['text'], 'url': i['link']})
        config['tts'] += f'Вы направились в категорию "Анонсы". {i["text"]} будет {i["date"]} '

    config['buttons'].insert(0, buttonsResponse)
    return createResponse(event, config)


def isTriggered(event):
    token = {"аннонс", "анонс", "анонсы"}
    return isSimilarTokens(event, token) and isInLastContext(event, 'news')


announces = {'getResponse': getResponse, 'isTriggered': isTriggered}
