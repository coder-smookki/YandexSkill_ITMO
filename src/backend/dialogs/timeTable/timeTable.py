from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    if not haveState(event, "timeTable_step"):
        config = copy.deepcopy(getConfig(event, "group"))
        config["session_state"]["timeTable_step"] = 1
        return createResponse(event, config)

    elif getState(event, "timeTable_step") == 1:
        config = copy.deepcopy(getConfig(event, "degree"))
        config["session_state"]["timeTable_step"] = 2
        config["session_state"]["timeTable_group"] = getCommand(event)
        return createResponse(event, config)

    degree = getOriginalUtterance(event)
    setStateInEvent(event, "timeTable_group", getState(event, "timeTable_group"))
    setStateInEvent(event, "timeTable_degree", degree)
    return allDialogs["timeTableFind"]["getResponse"](event, allDialogs)


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

    isAsk = (
        "еще" in getCommand(event)
        or "more" in getCommand(event)
        or "мор" in getCommand(event)
        or "моур" in getCommand(event)
        or "мар" in getCommand(event)
        or "маур" in getCommand(event)
    )
    isIs = (
        "занят" in getCommand(event)
        or "расп" in getCommand(event)
        or "time" in getCommand(event)
        or "тайм" in getCommand(event)
        or "таим" in getCommand(event)
        or "время" in getCommand(event)
    )

    if isInContext(event, "timeTable") and (isNextPage or isPastPage):
        return False

    return (
        isIs
        and isInContext(event, "mainMenu")
        or isInContext(event, "timeTable")
        or isInContext(event, "timeTable")
        and isAsk
    )


timeTable = {"getResponse": getResponse, "isTriggered": isTriggered}
