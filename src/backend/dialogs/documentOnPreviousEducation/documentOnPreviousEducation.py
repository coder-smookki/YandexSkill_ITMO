from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    return (
        (
            "пред" in getCommand(event)
            or "prev" in getCommand(event)
            or "прев" in getCommand(event)
            or "прив" in getCommand(event)
            or "паст" in getCommand(event)
        )
        and (
            "образ" in getCommand(event)
            or "обуч" in getCommand(event)
            or "lear" in getCommand(event)
            or "educ" in getCommand(event)
            or "едук" in getCommand(event)
            or "эдук" in getCommand(event)
            or "идук" in getCommand(event)
        )
    )


documentOnPreviousEducation = {"getResponse": getResponse, "isTriggered": isTriggered}
