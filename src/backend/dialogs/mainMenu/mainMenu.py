from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

def getResponse(event, allDialogs=None):
    config = getConfig(event)
    if not isInLastContext(event, 'mainMenu'):
        if 'русский' in getCommand(event) or 'рус' in getCommand(event) or 'ру' in getCommand(event):
            print('setted ru-RU')
            setGlobalStateInEvent(event, 'language', 'ru-RU')
        else:
            print('setted en-US')
            setGlobalStateInEvent(event, 'language', 'en-US')
    return createResponse(event, config)


def isTriggered(event):
    # return isSimilarTokens(event, {'главное', 'меню'})
    return True


mainMenu = {'getResponse': getResponse, 'isTriggered': isTriggered}
