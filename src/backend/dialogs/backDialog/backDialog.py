from utils.triggerHelper import *
from utils.branchHandler import *


def getResponse(event, allDialogs=None):
    return getDialogResponseFromEnd(event, 2, allDialogs)


def isTriggered(event):
    return isSimilarCommand(event, 'назад') or isSimilarCommand(event, 'back')


backDialog = {'getResponse': getResponse, 'isTriggered': isTriggered}
