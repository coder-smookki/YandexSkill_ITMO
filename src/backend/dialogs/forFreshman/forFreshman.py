from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    return (
        "первок" in getCommand(event)
        or "поступ" in getCommand(event)
        or "первок" in getCommand(event)
        or 'фрэш' in getCommand(event)
        or 'фреш' in getCommand(event)
        or 'fresh' in getCommand(event)
        or '' in getCommand(event)
        or 'первок' in getCommand(event)
        or 'первок' in getCommand(event)
        or 'первок' in getCommand(event)
        or 'первок' in getCommand(event)
        or 'первок' in getCommand(event)
    ) and isInLastContext(event, "mainMenu")


forFreshman = {"getResponse": getResponse, "isTriggered": isTriggered}
