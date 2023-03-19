from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()


def getResponse(event, allDialogs=None):
    return createResponse(event, config)


def isTriggered(event):
    return ("что" in getCommand(event) and (
        "умеешь" in getCommand(event)
        or "можешь" in getCommand(event)
        or "способен" in getCommand(event)
    )) or ("what" in getCommand(event) and (
        "can" in getCommand(event)
        or "capable" in getCommand(event)))


whatYouCan = {"getResponse": getResponse, "isTriggered": isTriggered}
