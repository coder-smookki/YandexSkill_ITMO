from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()


def getResponse(event, allDialogs=None):
    return createResponse(event, config)


def isTriggered(event):
    return "что" in getCommand(event) and (
        "умеешь" in getCommand(event)
        or "можешь" in getCommand(event)
        or "способен" in getCommand(event)
    )


news = {"getResponse": getResponse, "isTriggered": isTriggered}
