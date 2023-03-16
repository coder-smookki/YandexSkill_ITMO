from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    if not haveState(event, "timeTable_step"):
        config = copy.deepcopy(getConfig("group"))
        config["session_state"]["timeTable_step"] = 1
        return createResponse(event, config)

    elif getState(event, "timeTable_step") == 1:
        config = copy.deepcopy(getConfig("course"))
        config["session_state"]["timeTable_step"] = 2
        config["session_state"]["timeTable_group"] = getOriginalUtterance(event)
        return createResponse(event, config)

    elif getState(event, "timeTable_step") == 2:
        config = copy.deepcopy(getConfig("degree"))
        config["session_state"]["timeTable_step"] = 3
        config["session_state"]["timeTable_group"] = getState(event, "timeTable_group")
        config["session_state"]["timeTable_course"] = getOriginalUtterance(event)
        return createResponse(event, config)

    setStateInEvent(event, "timeTable_group", getState(event, "timeTable_group"))
    setStateInEvent(event, "timeTable_course", getState(event, "timeTable_course"))
    setStateInEvent(event, "timeTable_degree", getOriginalUtterance(event))
    return allDialogs["timeTableFind"]["getResponse"](event, allDialogs)


def isTriggered(event):
    token = {"занятий", "расписание", "расписание"}

    return (
        isSimilarTokens(event, token)
        and isInContext(event, "russianMenu")
        or isInContext(event, "timeTable")
    )


timeTable = {"getResponse": getResponse, "isTriggered": isTriggered}
