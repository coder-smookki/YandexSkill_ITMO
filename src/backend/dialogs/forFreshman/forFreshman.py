from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()


def getResponse(event, allDialogs=None):
    return createResponse(event, config)


def isTriggered(event):
    token = {"первокурсникам", "первокурс", "первокурсник", "первокурснкм", "первокрснкам"}
    print('isContext ' + str(isSimilarTokens(event, token)))
    return isSimilarTokens(event, token) and isInContext(event, 'russianMenu')


forFreshman = {'getResponse': getResponse, 'isTriggered': isTriggered}
