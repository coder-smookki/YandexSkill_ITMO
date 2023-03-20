from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *
from utils.globalStorage import globalStorage


def getResponse(event, allDialogs=None):
    config = getConfig()
    return createResponse(event, config)


def isTriggered(event):
    token = {"аннонс", "анонс", "анонсы"}
    return isSimilarTokens(event, token) and isInLastContext(event, 'news')


announces = {'getResponse': getResponse, 'isTriggered': isTriggered}
