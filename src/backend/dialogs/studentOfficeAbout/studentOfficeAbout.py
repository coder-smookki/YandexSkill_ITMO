from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    token = {"что", "такое", "what", "is"}
    return (
        "ват" in getCommand(event)
        or "уат" in getCommand(event)
        or "хат" in getCommand(event)
        or "уэт" in getCommand(event)
        or "ует" in getCommand(event)
        or "what" in getCommand(event)
        or ("что" in getCommand(event) and "такое" in getCommand(event))
    ) and isInContext(event, "studentOffice")
    # return isSimilarTokens(event, token) and isInContext(event, 'studentOffice')


studentOfficeAbout = {"getResponse": getResponse, "isTriggered": isTriggered}
