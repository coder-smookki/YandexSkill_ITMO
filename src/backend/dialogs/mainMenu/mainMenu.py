from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    if not isInLastContext(event, 'mainMenu'):
        if 'русский язык russian language' in getCommand(event) or 'рус' in getCommand(event) or 'ру' in getCommand(event):
            setGlobalStateInEvent(event, 'language', 'ru-RU')
        else:
            setGlobalStateInEvent(event, 'language', 'en-US')

    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    # return isSimilarTokens(event, {'главное', 'меню'})
    return True


mainMenu = {'getResponse': getResponse, 'isTriggered': isTriggered}
