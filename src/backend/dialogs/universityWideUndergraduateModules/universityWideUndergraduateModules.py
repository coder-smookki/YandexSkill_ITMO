from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    return (
        "уайд" in getCommand(event)
        or "уайт" in getCommand(event)
        or "модул" in getCommand(event)
        or "wide" in getCommand(event)
        or "modul" in getCommand(event)
    ) and isInContext(event, "mainMenu")


universityWideUndergraduateModules = {
    "getResponse": getResponse,
    "isTriggered": isTriggered,
}
