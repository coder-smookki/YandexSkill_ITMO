from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    return (
        "офис" in getCommand(event)
        or "афис" in getCommand(event)
        or "офес" in getCommand(event)
        or "афес" in getCommand(event)
        or "office" in getCommand(event)
    ) and isInLastContext(event, "mainMenu")


studentOffice = {"getResponse": getResponse, "isTriggered": isTriggered}
