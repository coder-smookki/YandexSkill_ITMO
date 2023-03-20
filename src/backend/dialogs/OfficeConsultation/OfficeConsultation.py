from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    return (
        "конс" in getCommand(event)
        or "cons" in getCommand(event)
        or "канс" in getCommand(event)
        or "кэнс" in getCommand(event)
        or "кенс" in getCommand(event)
        or "попас" in getCommand(event)
    ) and isInContext(event, "studentOffice")


OfficeConsultation = {"getResponse": getResponse, "isTriggered": isTriggered}
