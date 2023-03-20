from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    token = {"стипендии", "степуха", "scholarships"}
    return (
        "стип" in getCommand(event)
        or "степ" in getCommand(event)
        or "школ" in getCommand(event)
        or "ш" in getCommand(event)
    ) and isInContext(event, "mainMenu")


scholarships = {"getResponse": getResponse, "isTriggered": isTriggered}
