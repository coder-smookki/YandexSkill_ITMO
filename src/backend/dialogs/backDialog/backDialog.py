from utils.triggerHelper import *
from utils.branchHandler import *


def getResponse(event, allDialogs=None):
    return getDialogResponseFromEnd(event, 2, allDialogs)


def isTriggered(event):
    return isSimilarCommand(event, 'назад')


backDialog = {'getResponse': getResponse, 'isTriggered': isTriggered}
