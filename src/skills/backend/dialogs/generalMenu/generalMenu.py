from .config import getConfig
from ..utils.dialogCreator import *
from ..utils.triggerHelper import *


def getResponse(event, context):
    config = getConfig()
    return createResponse(event, config)


def isTriggered(event, context):
    return isNewSession(event)


generalMenu = {'getResponse': getResponse, 'isTriggered': isTriggered}
