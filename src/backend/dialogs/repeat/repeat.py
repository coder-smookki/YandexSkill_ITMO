from .config import getConfig
from utils.triggerHelper import *
from utils.responseHelper import *
from utils.branchHandler import getDialogResponseFromEnd

config = getConfig()


def getResponse(event, allDialogs=None):
    return allDialogs[getState('branch')[-1]]['getResponse'](event, allDialogs)

def isTriggered(event):
    return (
        "повтори" in getCommand(event)
        or "еще раз" in getCommand(event)
        or "еще раз" in getCommand(event)
)


repeat = {"getResponse": getResponse, "isTriggered": isTriggered}
