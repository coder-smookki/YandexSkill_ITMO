from .config import getConfig
from utils.dialogCreator import *
from utils.triggerHelper import *

config = getConfig()
def getResponse(event, context):
    return createResponse(event, config)


def isTriggered(event, context):
    return isNewSession(event)


generalMenu = {'getResponse': getResponse, 'isTriggered': isTriggered}
