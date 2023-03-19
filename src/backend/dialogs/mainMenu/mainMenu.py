from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

def getResponse(event, allDialogs=None):
    config = getConfig(event)
    if isInLastContext('chooseLanguage'):
        if 'русский' in getCommand(event) or 'рус' in getCommand(event) or 'ру' in getCommand(event)
            setGlobalStateInEvent(event, 'language', 'ru-RU')
        else:
            setGlobalStateInEvent(event, 'language', 'en-US')
    a = createResponse(event, config)
    # print(a)
    return a


def isTriggered(event):
    # return isSimilarTokens(event, {'главное', 'меню'})
    return True


mainMenu = {'getResponse': getResponse, 'isTriggered': isTriggered}
