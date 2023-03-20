from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    token = {"общеуниверситетские", "модули", "university-wide", "modules"}
    return isSimilarTokens(event, token) and 'магис' in getCommand(event) and isInContext(event, 'mainMenu')


universityWideMagistracyModules = {'getResponse': getResponse, 'isTriggered': isTriggered}
