from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *
from utils.globalStorage import globalStorage


def getResponse(event, allDialogs=None):
    config = getConfig()
    return createResponse(event, config)


def isTriggered(event):
    token = {"аннонс", "анонс", "анонсы"}
    return (
        "аннонс" in getCommand(event)
        or "анонс" in getCommand(event)
        or "аноус" in getCommand(event)
        or "анноус" in getCommand(event)
        or "анус" in getCommand(event)
        or "аннус" in getCommand(event)
        or "announ" in getCommand(event)
    )


announces = {"getResponse": getResponse, "isTriggered": isTriggered}
