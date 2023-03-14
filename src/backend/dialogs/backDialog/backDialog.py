from utils.triggerHelper import *
from utils.branchHandler import *

def getResponse(event, allDialogs=None):
    return getDialogResponseFromEnd(event, 1, allDialogs)

def isTriggered(event):
    return isSimilarCommand(event, 'назад')

backDialog = {'getResponse': getResponse, 'isTriggered': isTriggered}