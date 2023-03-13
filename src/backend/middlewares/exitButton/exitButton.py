from utils.responseHelper import *
from utils.triggerHelper import *
from dialogs.russianMenu.russianMenu import russianMenu
def getResponse(event, allDialogs):
    return allDialogs['russianMenu']['getResponse'](event, None)

def isTriggered(event, context):
    return isSimilarCommand(event, "Выйти")

exitButton = {'getResponse': getResponse, 'isTriggered': isTriggered}
