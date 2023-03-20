from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    token = {"студенческий", "студенчески", "студенческ", "офис", "офисс", "офи", 'student', 'office'}
    return isSimilarTokens(event, token) and isInLastContext(event, 'mainMenu')


studentOffice = {'getResponse': getResponse, 'isTriggered': isTriggered}
