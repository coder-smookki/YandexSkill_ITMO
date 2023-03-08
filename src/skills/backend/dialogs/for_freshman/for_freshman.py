from .config import getConfig
from ..utils.dialogCreator import *
from ..utils.triggerHelper import *


def getResponse(event, context):
    config = getConfig()
    return createResponse(event, config)


def isTriggered(event):
    token = {"первокурсникам", "первокурс", "первокурсник", "первокурснкм", "первокрснкам"}
    return isSimilarTokens(event, token)


for_freshman = {'getResponse': getResponse, 'isTriggered': isTriggered}
