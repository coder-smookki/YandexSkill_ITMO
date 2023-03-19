from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    changeLangTokens = {'язык', 'language', 'lang'}
    if isInLastContext(event, 'mainMenu') and isSimilarTokens(event, changeLangTokens):
        return allDialogs['chooseLanguage']['getResponse'](event, allDialogs)
    print('state language:', getGlobalState(event, 'language'))
    print('getLanguage:', getLanguage(event))
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    # return isSimilarTokens(event, {'главное', 'меню'})
    return True


mainMenu = {'getResponse': getResponse, 'isTriggered': isTriggered}
