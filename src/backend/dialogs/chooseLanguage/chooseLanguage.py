from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()


def getResponse(event, allDialogs=None):
    return createResponse(event, config)


def isTriggered(event):
    tokens = {'язык', 'language', 'lang'}
    return not haveGlobalState(event, 'language') or isSimilarTokens(event, tokens) and isInLastContext(event, 'mainMenu')


chooseLanguage = {'getResponse': getResponse, 'isTriggered': isTriggered}
