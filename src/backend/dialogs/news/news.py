from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()
def getResponse(event, context):
    return createResponse(event, config)


def isTriggered(event, context):
    token = {"новости", "новость", "новост"}
    return isSimilarTokens(event, token) and isInContext(event, 'generalMenu')


news = {'getResponse': getResponse, 'isTriggered': isTriggered}
