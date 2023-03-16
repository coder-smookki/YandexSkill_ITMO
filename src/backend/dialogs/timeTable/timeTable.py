from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

def getResponse(event, allDialogs=None):
    if not haveState(event, 'group'):
        config = getConfig('group')
        return createResponse(event, config)
    elif not haveState(event, 'course'):
        config = getConfig('course')
        return createResponse(event, config)
    return allDialogs['timeTableFind']['getResponse'](event, allDialogs)


def isTriggered(event):
    token = {"занятий", "расписание", "расписание"}

    return isSimilarTokens(event, token) and isInContext(event, 'russianMenu') or isInContext('timeTable')


timeTable = {'getResponse': getResponse, 'isTriggered': isTriggered}
