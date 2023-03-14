from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()
def getResponse(event, context):
    return createResponse(event, config)


def isTriggered(event, context):
    token = {"аннонс", "анонс", "анонсы"}
    return isSimilarTokens(event, token) and isInContext(event, 'news')


announces = {'getResponse': getResponse, 'isTriggered': isTriggered}