from utils.triggerHelper import *
from utils.branchHandler import *
from utils.responseHelper import getCommand

def getResponse(event, allDialogs=None):
    return getDialogResponseFromEnd(event, 2, allDialogs)


def isTriggered(event):
    return 'назад' in getCommand(event) or 'бэк' in getCommand(event) or 'бек' in getCommand(event) or 'back' in getCommand(event)


backDialog = {'getResponse': getResponse, 'isTriggered': isTriggered}
