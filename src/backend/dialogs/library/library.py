from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    token = {"библиотека", "книжная", "библиоте", "library"}
    return isSimilarTokens(event, token) and isInContext(event, 'mainMenu')


library = {'getResponse': getResponse, 'isTriggered': isTriggered}
