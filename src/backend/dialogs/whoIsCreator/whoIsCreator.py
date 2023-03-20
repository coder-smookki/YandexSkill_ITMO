from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    return (
        "who" in getCommand(event)
        or "creator" in getCommand(event)
        or "ху" in getCommand(event)
        or "креа" in getCommand(event)
        or "креэ" in getCommand(event)
        or "крэ" in getCommand(event)
        or "созда" in getCommand(event)
        or "сдела" in getCommand(event)
        or "разраб" in getCommand(event)
        or "прогр" in getCommand(event)
    )


whoIsCreator = {"getResponse": getResponse, "isTriggered": isTriggered}
