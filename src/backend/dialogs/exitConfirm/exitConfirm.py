from .config import getConfig
from utils.triggerHelper import *
from utils.responseHelper import *
from utils.branchHandler import getDialogResponseFromEnd
import copy

config = getConfig()
def getResponse(event, allDialogs=None):
    if isInContext(event, 'exitConfirm') and isSimilarCommand(event, 'да'):
        newConfig = copy.deepcopy(config)
        newConfig['end_session'] = True
        return createResponse(event, newConfig)
    elif isInContext(event, 'exitConfirm'):
        return getDialogResponseFromEnd(event, 2, allDialogs)
    return createResponse(event, config)


def isTriggered(event):
    return isSimilarCommand(event, 'выйти') or isInContext(event, 'exitConfirm') and isSimilarCommand(event, 'да')


exitConfirm = {'getResponse': getResponse, 'isTriggered': isTriggered}
