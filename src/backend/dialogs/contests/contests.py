from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *
from utils.globalStorage import globalStorage


def getResponse(event, allDialogs=None):
    config = getConfig()

    return createResponse(event, config)


def isTriggered(event):
    token = {"контесты", "контест", "контестс"}
    return (
        "контест" in getCommand(event)
        or "контэст" in getCommand(event)
        or "конкурс" in getCommand(event)
        or 'contest' in getCommand(event)
    ) and isInContext(event, 'news')


contests = {"getResponse": getResponse, "isTriggered": isTriggered}
