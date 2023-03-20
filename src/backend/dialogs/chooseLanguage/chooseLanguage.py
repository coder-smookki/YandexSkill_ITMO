from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()


def getResponse(event, allDialogs=None):
    return createResponse(event, config)


def isTriggered(event):
    return (
        "ланг" in getCommand(event)
        or "лэнг" in getCommand(event)
        or "ленг" in getCommand(event)
        or "лонг" in getCommand(event)
        or "lang" in getCommand(event)
        or "язык" in getCommand(event)
        or "езык" in getCommand(event)
    ) and not isInLastContext('mainMenu')


chooseLanguage = {"getResponse": getResponse, "isTriggered": isTriggered}
