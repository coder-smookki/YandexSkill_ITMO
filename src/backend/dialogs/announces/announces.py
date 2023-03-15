from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *
from utils.globalStorage import globalStorage

def getResponse(event, allDialogs=None):
    config = getConfig()
    announces = globalStorage['news_announces']

    for i in announces:
        config['message'] += f"""
        {i['text']}.\n
        {i['link']}.\n
        {i['date']}.\n
        ------------\n
        """
        config['tts'] += f'Вы направились в категорию "Анонсы". {i["text"]} будет {i["date"]} '
    return createResponse(event, config)


def isTriggered(event):
    token = {"аннонс", "анонс", "анонсы"}
    return isSimilarTokens(event, token) and isInContext(event, 'news')


announces = {'getResponse': getResponse, 'isTriggered': isTriggered}