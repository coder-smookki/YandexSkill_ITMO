from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

def getResponse(event, allDialogs=None):
    if not haveState(event, 'timeTable_group'):
        print('1')
        config = copy.deepcopy(getConfig('group'))
        config['session_state']['timeTable_group'] = 'notEntered'
        return createResponse(event, config)
    
    elif not haveState(event, 'timeTable_course'):
        print('2')
        config = copy.deepcopy(getConfig('course'))
        config['session_state']['timeTable_course'] = 'notEntered'
        config['session_state']['timeTable_group'] = getOriginalUtterance(event)
        return createResponse(event, config)
    
    setStateInEvent(event, 'timeTable_group', getState(event, 'timeTable_group'))
    setStateInEvent(event, 'timeTable_course', getOriginalUtterance(event))
    return allDialogs['timeTableFind']['getResponse'](event, allDialogs)


def isTriggered(event):
    token = {"занятий", "расписание", "расписание"}

    return isSimilarTokens(event, token) and isInContext(event, 'russianMenu') or isInContext(event, 'timeTable')


timeTable = {'getResponse': getResponse, 'isTriggered': isTriggered}
