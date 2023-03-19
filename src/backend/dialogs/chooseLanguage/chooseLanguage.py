from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()


def getResponse(event, allDialogs=None):
    return createResponse(event, config)


def isTriggered(event):
    return False


chooseLanguage = {'getResponse': getResponse, 'isTriggered': isTriggered}
