from utils.responseHelper import *
from utils.triggerHelper import *
from dialogs.russianMenu.russianMenu import russianMenu
def getResponse(event, allDialogs):
    if not 'branch' in event['state']['session']:
        return allDialogs['russianMenu']['getResponse'](event, None)

    branch = event['state']['session']["branch"] 
    return allDialogs[branch]['getResponse'](event, None)

def isTriggered(event, context):
    return isSimilarCommand(event, "Назад")

exitButton = {'getResponse': getResponse, 'isTriggered': isTriggered}
