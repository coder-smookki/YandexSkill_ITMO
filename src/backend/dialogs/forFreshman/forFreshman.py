from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    token = {"первокурсникам", "первокурс", "первокурсник", "первокурснкм", "первокрснкам"}
    return isSimilarTokens(event, token) and isInContext(event, 'mainMenu')


forFreshman = {'getResponse': getResponse, 'isTriggered': isTriggered}
