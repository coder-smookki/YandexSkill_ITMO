from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()
def getResponse(event, context):
    return createResponse(event, config)


def isTriggered(event, context):
    token = {"первокурсникам", "первокурс", "первокурсник", "первокурснкм", "первокрснкам"}
    return isSimilarTokens(event, token) and isInContext(event, 'generalMenu')


forFreshman = {'getResponse': getResponse, 'isTriggered': isTriggered}
