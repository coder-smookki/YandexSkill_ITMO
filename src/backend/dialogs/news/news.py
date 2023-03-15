from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()


def getResponse(event, allDialogs=None):
    return createResponse(event, config)


def isTriggered(event):
    token = {"новости", "новость", "новост"}
    return isSimilarTokens(event, token) and isInContext(event, 'russianMenu')


news = {'getResponse': getResponse, 'isTriggered': isTriggered}
