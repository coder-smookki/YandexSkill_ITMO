from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    print('command:', getCommand(event))
    print('orgiUtter:', getOriginalUtterance(event))
    if not haveState(event, "timeTable_step"):
        config = copy.deepcopy(getConfig("group"))
        config["session_state"]["timeTable_step"] = 1
        return createResponse(event, config)

    elif getState(event, "timeTable_step") == 1:
        config = copy.deepcopy(getConfig("degree"))
        config["session_state"]["timeTable_step"] = 2
        config["session_state"]["timeTable_group"] = getOriginalUtterance(event)
        return createResponse(event, config)

    degree = getOriginalUtterance(event)
    setStateInEvent(event, "timeTable_group", getState(event, "timeTable_group"))
    setStateInEvent(event, "timeTable_degree", degree)
    return allDialogs["timeTableFind"]["getResponse"](event, allDialogs)


def isTriggered(event):
    token = {"занятий", "расписание", "расписание"}
    askToken = {"еще", "заново", "ещё", "заново"}
    nextPageTokens = {"дальше", "далее", "следующая", "некст", "следующий"}
    pastPageTokens = {"предыдущая", "обратно"}

    if isInContext(event, "timeTable") and (
            isSimilarTokens(event, nextPageTokens) or isSimilarTokens(event, pastPageTokens)):
        return False

    return (
            isSimilarTokens(event, token)
            and isInContext(event, "mainMenu")
            or isInContext(event, "timeTable")
            or isInContext(event, "timeTable")
            and isSimilarTokens(event, askToken)
    )


timeTable = {"getResponse": getResponse, "isTriggered": isTriggered}
