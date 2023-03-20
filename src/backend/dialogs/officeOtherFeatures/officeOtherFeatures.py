from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    return (
        "вопр" in getCommand(event)
        or "прос" in getCommand(event)
        or "помож" in getCommand(event)
        or "help" in getCommand(event)
        or "хелп" in getCommand(event)
        or "аск" in getCommand(event)
        or "куэш" in getCommand(event)
        or "куеш" in getCommand(event)
        or "каэш" in getCommand(event)
        or "каеш" in getCommand(event)
        or "куш" in getCommand(event)
        or "каш" in getCommand(event)
        or "кеш" in getCommand(event)
        or "que" in getCommand(event)
        or "ans" in getCommand(event)
    ) and isInContext(event, "studentOffice")


officeOtherFeatures = {"getResponse": getResponse, "isTriggered": isTriggered}
