from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()


def getResponse(event, allDialogs=None):
    return createResponse(event, config)


def isTriggered(event):
    token = {"студенческий", "студенчески", "студенческ", "офис", "офисс", "офи"}
    return isSimilarTokens(event, token) and isInLastContext(event, 'russianMenu')


studentOffice = {'getResponse': getResponse, 'isTriggered': isTriggered}
