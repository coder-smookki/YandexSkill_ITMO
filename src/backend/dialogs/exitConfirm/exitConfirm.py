from .config import getConfig
from utils.triggerHelper import *
from utils.responseHelper import *

config = getConfig()
def getResponse(event, context):
    return createResponse(event, config)

def isTriggered(event, context):
    return isSimilarCommand('выйти')