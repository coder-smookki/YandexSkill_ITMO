from .config import *
from utils.responseHelper import *
from utils.triggerHelper import *
from utils.branchHandler import getDialogResponseFromEnd

mainConfig = getMainConfig()
bechelorConfig = getBechelorConfig()
magistracyConfig = getMagistracyConfig()
internationalMagistracyConfig = getInternationalMagistracyConfig()
additionalOpportsConfig = getAdditionalOpportsConfig()
migrationDocumentsConfig = getMigrationDocumentsConfig()


def getResponse(event, allDialogs=None):
    if not isInLastContext(event, 'toAForeignStudent'):
        return createResponse(event, mainConfig)

    if 'бакал' in getCommand(event):
        return createResponse(event, bechelorConfig)

    if ('между' in getCommand(event) or 'народ' in getCommand(event)) and 'магис' in getCommand(event):
        return createResponse(event, internationalMagistracyConfig)

    if 'магис' in getCommand(event):
        return createResponse(event, magistracyConfig)

    if 'докум' in getCommand(event):
        return createResponse(event, migrationDocumentsConfig)

    if 'возм' in getCommand(event) or 'доп' in getCommand(event):
        return createResponse(event, additionalOpportsConfig)

    return createResponse(event, mainConfig)


def isTriggered(event):
    token = {"иностранный", "иностранному", "иностранцу"}
    return isInLastContext(event, 'toAForeignStudent') or isSimilarTokens(event, token) and isInContext(event,
                                                                                                        'mainMenu')


toAForeignStudent = {'getResponse': getResponse, 'isTriggered': isTriggered}
