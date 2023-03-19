from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    if not isInLastContext(event, 'mainMenu'):
        print('notLastContext')
        if 'рус' in getCommand(event):
            print('ru in command')
            setGlobalStateInEvent(event, 'language', 'ru-RU')
        else:
            print('else in command')
            setGlobalStateInEvent(event, 'language', 'en-US')

    changeLangTokens = {'язык', 'language', 'lang'}
    if isSimilarTokens(event, changeLangTokens):
        return allDialogs['changeLanguage']['getResponse'](event, allDialogs)
    print('state language:', getGlobalState(event, 'language'))
    print('getLanguage:', getLanguage(event))
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    # return isSimilarTokens(event, {'главное', 'меню'})
    return True


mainMenu = {'getResponse': getResponse, 'isTriggered': isTriggered}
