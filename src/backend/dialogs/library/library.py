from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    return (
        "библ" in getCommand(event)
        or "libr" in getCommand(event)
        or "либ" in getCommand(event)
        or "лайб" in getCommand(event)
        or "лийб" in getCommand(event)
        or "лэйб" in getCommand(event)
        or "лейб" in getCommand(event)
    ) and isInLastContext(event, "mainMenu")


library = {"getResponse": getResponse, "isTriggered": isTriggered}
