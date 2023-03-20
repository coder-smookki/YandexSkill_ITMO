from utils.triggerHelper import *
from utils.branchHandler import *
from utils.responseHelper import getCommand


def getResponse(event, allDialogs=None):
    return getDialogResponseFromEnd(event, 2, allDialogs)


def isTriggered(event):
    words = ["назад", "back", "бэк", "бек"]

    return isInCommandOr(event, words)


backDialog = {"getResponse": getResponse, "isTriggered": isTriggered}
