from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *
from utils.globalStorage import globalStorage

def getResponse(event, allDialogs=None):
    config = getConfig()
    contests = globalStorage['news_contests']

    for i in contests:
        config['message'] += f"""
        {i['text']}\n
        {i['link']}\n
        {i['date']}\n
        ------------\n
        """
        config['tts'] += f'Вы направились в категорию "Контесты". {i["text"]} будет {i["date"]} '
    return createResponse(event, config)


def isTriggered(event):
    token = {"контесты", "контест", "контестс"}
    return isSimilarTokens(event, token) and isInContext(event, 'news')


contests = {'getResponse': getResponse, 'isTriggered': isTriggered}
