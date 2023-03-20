from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    return (
        "зачем" in getCommand(event)
        or "вай" in getCommand(event)
        or "уай" in getCommand(event)
        or "уэй" in getCommand(event)
        or "уей" in getCommand(event)
        or "ваи" in getCommand(event)
        or "уаи" in getCommand(event)
        or "уэи" in getCommand(event)
        or "уеи" in getCommand(event)
        or "why" in getCommand(event)
    ) and isInContext(event, "studentOffice")


studentOfficeWhy = {"getResponse": getResponse, "isTriggered": isTriggered}
