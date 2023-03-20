from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    token = {"общеуниверситетские", "модули", "university-wide", "modules"}

    return (
        (
            "уайд" in getCommand(event)
            or "уайт" in getCommand(event)
            or "модул" in getCommand(event)
            or "wide" in getCommand(event)
            or "modul" in getCommand(event)
        )
        and (
            "магис" in getCommand(event)
            or "magis" in getCommand(event)
            or "могис" in getCommand(event)
            or "магес" in getCommand(event)
            or "магэс" in getCommand(event)
            or "могес" in getCommand(event)
        )
        and isInContext(event, "mainMenu")
    )


universityWideMagistracyModules = {
    "getResponse": getResponse,
    "isTriggered": isTriggered,
}
