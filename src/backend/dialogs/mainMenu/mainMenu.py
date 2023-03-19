from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    if isNewSession(event) and not haveGlobalState(event, 'language'):
        return allDialogs['chooseLanguage']['getResponse'](event, allDialogs)

    print(event['request']['nlu']['tokens'])
    if isInLastContext(event, 'chooseLanguage'):
        print('choosLang context')
        if 'рус' in getCommand(event) or  'рас' in getCommand(event) or 'rus' in getCommand(event):
            print('rus tokens')
            setGlobalStateInEvent(event, 'language', 'ru-RU')
        else:
            print('another tokens')
            setGlobalStateInEvent(event, 'language', 'en-US')

    print('state language:', getGlobalState(event, 'language'))
    print('getLanguage:', getLanguage(event))
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    # return isSimilarTokens(event, {'главное', 'меню'})
    return True


mainMenu = {'getResponse': getResponse, 'isTriggered': isTriggered}
