from utils.triggerHelper import *
from utils.branchHandler import *

def getResponse(event, context):
    return getDialogResponseFromEnd(event, 1)

def isTriggered(event, context):
    return isSimilarCommand('назад')

backDialog = {'getResponse': getResponse, 'isTriggered': isTriggered}