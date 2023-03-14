import copy
from .responseHelper import createResponse
from dialogs.allDialogs import allDialogs

def updateBranchToResponse(event, response):
    newEvent = copy.deepcopy(event)
    newResponse = copy.deepcopy(response)

    if not 'branch' in newEvent['state']['session']:
        eventBranch = newEvent['state']['session']['branch']
        newResponse['session_state']['branch'] = eventBranch
        return newResponse
    else:
        eventBranch = newEvent['state']['session']['branch']
        responseState = newResponse['session_state']['branch']
        # сработает, если eventbranch.index(...) найдет новый брэнч в брэнчах
        try:
            index = eventBranch.index(responseState)
            eventBranch = eventBranch[0:index + 1]
            newResponse['session_state']['branch'] = eventBranch
            return newResponse
        # в случае, если в брэнчах нету нового бренча
        except:
            eventBranch.append(responseState)
            response['session_state']['branch'] = eventBranch
            return response

def getDialogResponseFromEnd(event, dialogNumber):
    branchList = event["state"]["session"]["branch"]
    if dialogNumber > len(branchList):
        return allDialogs[branchList[0]]['getResponse'](event, None)
    return allDialogs[branchList[-dialogNumber]]['getResponse'](event, None)



