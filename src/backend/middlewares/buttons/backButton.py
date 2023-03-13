from utils.responseHelper import *
from utils.triggerHelper import *

def getResponse(event, allDialogs):
    if not 'branch' in event['state']['session']:
        return allDialogs['russianMenu']['getResponse'](event, None)

    branch = event['state']['session']["branch"] 
    return allDialogs[branch]['getResponse'](event, None)

def isTriggered(event, context):
    print(isSimilarCommand(event, "Назад"))
    return isSimilarCommand(event, "Назад")

backButton = {'getResponse': getResponse, 'isTriggered': isTriggered}
