from .config import getConfig
from ..utils.dialogCreator import *
from ..utils.triggerHelper import *


def getResponse(event, context):
    config = getConfig()
    return createResponse(event, config)


def isTriggered(event, context):
    token = {"контесты", "контест", "контестс"}
    return isSimilarTokens(event, token) and isInContext(event, 'news')


contests = {'getResponse': getResponse, 'isTriggered': isTriggered}
