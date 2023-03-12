from .config import getConfig
from ..utils.dialogCreator import *
from ..utils.triggerHelper import *


def getResponse(event, context):
    config = getConfig()
    return createResponse(event, config)


def isTriggered(event, context):
    token = {"аннонс", "анонс", "анонсы"}
    return isSimilarTokens(event, token) and isInContext(event, 'news')


announces = {'getResponse': getResponse, 'isTriggered': isTriggered}
