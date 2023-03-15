from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *
from utils.globalStorage import *
import copy

origConfig = getConfig()
def getResponse(event, allDialogs=None):
    info = globalStorage['sessionId']
    config = copy.deepcopy(origConfig)
    for elem in info:
        config['buttons'].insert(0, {
            'title': str(info.index(elem)),
            'url': elem['link']
        })

        config['message'] += f"""
                {str(info.index(elem)) + '. ' + elem['title']}.\n
                {elem['text']}.\n
                ------------\n
            """
    return createResponse(event, config)


def isTriggered(event):
    token = {"учебные", "издания", "учебны"}
    return isSimilarTokens(event, token) and isInContext(event, 'russianMenu')


educationalPublications = {
    'getResponse': getResponse, 'isTriggered': isTriggered}
