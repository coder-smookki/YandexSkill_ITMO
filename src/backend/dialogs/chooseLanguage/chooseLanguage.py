from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()


def getResponse(event, allDialogs=None):
    return createResponse(event, config)


def isTriggered(event):
    changeLangTokens = {'язык', 'language', 'lang'}
    return isInLastContext(event, 'mainMenu') and isSimilarTokens(event, changeLangTokens)


chooseLanguage = {'getResponse': getResponse, 'isTriggered': isTriggered}
