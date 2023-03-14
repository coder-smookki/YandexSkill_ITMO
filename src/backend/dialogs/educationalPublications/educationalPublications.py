from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()
def getResponse(event, context):
    return createResponse(event, config)


def isTriggered(event, context):
    token = {"учебные", "издания", "учебны"}
    return isSimilarTokens(event, token) and isInContext(event, 'russianMenu')


educationalPublications = {'getResponse': getResponse, 'isTriggered': isTriggered}