from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()
def getResponse(event, allDialogs=None):
    return createResponse(event, config)


def isTriggered(event):
    token = {"занятий", "расписание", "расписание"}
    return isSimilarTokens(event, token) and isInContext(event, 'russianMenu')


timeTable = {'getResponse': getResponse, 'isTriggered': isTriggered}
