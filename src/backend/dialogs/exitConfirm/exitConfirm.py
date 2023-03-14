from .config import getConfig
from utils.triggerHelper import *
from utils.responseHelper import *

config = getConfig()
def getResponse(event, allDialogs=None):
    return createResponse(event, config)

def isTriggered(event):
    return isSimilarCommand(event, 'выйти')

exitConfirm = {'getResponse': getResponse, 'isTriggered': isTriggered}