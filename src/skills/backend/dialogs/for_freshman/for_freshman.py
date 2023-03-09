from .config import getConfig
from ..utils.dialogCreator import *
from ..utils.triggerHelper import *
def getResponse(event, context):
    config = getConfig()
    return createResponse(event, config)


def isTriggered(event, context):
    token = {"первокурсникам", "первокурс", "первокурсник", "первокурснкм", "первокрснкам"}
    return isSimilarTokens(event, token) and isInContext(event, 'generalMenu')


for_freshman = {'dialogContext': 'for_freshman', 'getResponse': getResponse, 'isTriggered': isTriggered}