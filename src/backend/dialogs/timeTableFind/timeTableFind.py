from .config import *
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    isNextPage = (
        "след" in getCommand(event)
        or "дал" in getCommand(event)
        or "некст" in getCommand(event)
        or "next" in getCommand(event)
        or "нэкст" in getCommand(event)
    )

    isPastPage = (
        "наз" in getCommand(event)
        or "обр" in getCommand(event)
        or "прэв" in getCommand(event)
        or "прив" in getCommand(event)
        or "prev" in getCommand(event)
        or "прев" in getCommand(event)
    )

    countOnOnePage = 2
    if isNextPage:
        lastPage = getState(event, "timeTable_lastPage")
        config = getPageConfig(event, lastPage + 1, countOnOnePage)
    elif isPastPage:
        lastPage = getState(event, "timeTable_lastPage")
        config = getPageConfig(event, lastPage - 1, countOnOnePage)
    else:
        config = getConfig(event, countOnOnePage)
    return createResponse(event, config)


def isTriggered(event):
    isNextPage = (
        "след" in getCommand(event)
        or "дал" in getCommand(event)
        or "некст" in getCommand(event)
        or "next" in getCommand(event)
        or "нэкст" in getCommand(event)
    )

    isPastPage = (
        "наз" in getCommand(event)
        or "обр" in getCommand(event)
        or "прэв" in getCommand(event)
        or "прив" in getCommand(event)
        or "prev" in getCommand(event)
        or "прев" in getCommand(event)
    )
    return isInContext(event, "timeTable") and (isNextPage or isPastPage)


timeTableFind = {"getResponse": getResponse, "isTriggered": isTriggered}
