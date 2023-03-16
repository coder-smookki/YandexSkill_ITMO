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

    degree = getOriginalUtterance(event)
    if 'бакал' in degree or 'unde' in degree:
        degree = 3
    elif 'магис' in degree or 'magis' in degree: 
        degree = 4
    elif 'спец' in degree or 'spec' in degree: 
        degree = 4
    else:
        raise ValueError("Сould not recognize degree: " + degree)


    setStateInEvent(event, "timeTable_group", getState(event, "timeTable_group"))
    setStateInEvent(event, "timeTable_course", getState(event, "timeTable_course"))
    setStateInEvent(event, "timeTable_degree", degree)
    return allDialogs["timeTableFind"]["getResponse"](event, allDialogs)


def isTriggered(event):
    token = {"занятий", "расписание", "расписание"}

    return (
        isSimilarTokens(event, token)
        and isInContext(event, "russianMenu")
        or isInContext(event, "timeTable")
    )


timeTable = {"getResponse": getResponse, "isTriggered": isTriggered}
