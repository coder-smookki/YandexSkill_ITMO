from .config import getConfig
from utils.triggerHelper import *
from utils.responseHelper import *
import copy

config = getConfig()
def getResponse(event, allDialogs=None):
    if 'wanttoexit' in event['state']['session']:
        newConfig = copy.deepcopy(config)
        newConfig['end_session'] = True
        return createResponse(event, newConfig)
        
    return createResponse(event, config)

def isTriggered(event):
    return isSimilarCommand(event, 'выйти') or isInContext(event, 'exitConfirm') and haveState(event, 'wanttoexit') and isSimilarCommand(event, 'да')

exitConfirm = {'getResponse': getResponse, 'isTriggered': isTriggered}