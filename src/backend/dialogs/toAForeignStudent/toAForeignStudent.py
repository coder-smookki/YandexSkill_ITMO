from .config import *
from utils.responseHelper import *
from utils.triggerHelper import *
from utils.branchHandler import getDialogResponseFromEnd


def getResponse(event, allDialogs=None):
    return createResponse(event, getMainConfig(event))

def isTriggered(event):
    return (
            "между" in getCommand(event)
            or "народ" in getCommand(event)
            or "inter" in getCommand(event)
            or "интер" in getCommand(event)
            or "nation" in getCommand(event)
            or "иност" in getCommand(event)
            or "мигр" in getCommand(event)
            or "fore" in getCommand(event)
            or "форэ" in getCommand(event)
            or "фарэ" in getCommand(event)
            or "форе" in getCommand(event)
            or "фаре" in getCommand(event)
            or "фэрэ" in getCommand(event)
            or "фэре" in getCommand(event)
        ) and isInContext(event, "mainMenu")
    



def getBenchResponse(event, allDialogs):
    return createResponse(event, getBechelorConfig(event))
    
def isTriggeredBench(event):
    return (
        "бакал" in getCommand(event)
        or "bec" in getCommand(event)
        or "bac" in getCommand(event)
        or "бэнч" in getCommand(event)
        or "банч" in getCommand(event)
        or "бэч" in getCommand(event)
        or "бач" in getCommand(event)
    ) or isInLastContext(event, 'toAForeignStudent')
        


def getInterResponse(event, allDialogs):
    return createResponse(event, getInternationalMagistracyConfig(event))

def isTriggeredInter(event):
    return ((
        "между" in getCommand(event)
        or "народ" in getCommand(event)
        or "inter" in getCommand(event)
        or "интер" in getCommand(event)
        or "nation" in getCommand(event)
    ) and (
        "магис" in getCommand(event)
        or "mast" in getCommand(event)
        or "magic" in getCommand(event)
        or "magis" in getCommand(event)
        or "мег" in getCommand(event)
        or "мэг" in getCommand(event)
        or "mast" in getCommand(event)
        or "маст" in getCommand(event)
        or "маг" in getCommand(event)
    )) or isInLastContext(event, 'toAForeignStudent')



def getResponseMag(event, allDialogs):
    return createResponse(event, getMagistracyConfig(event))

def isTriggeredMag(event):
    return (
        "магис" in getCommand(event)
        or "magic" in getCommand(event)
        or "magis" in getCommand(event)
        or "mast" in getCommand(event)
        or "маст" in getCommand(event)
        or "мег" in getCommand(event)
        or "мэг" in getCommand(event)
        or "маг" in getCommand(event)
    ) or isInLastContext(event, 'toAForeignStudent')



def isTriggeredDocum(event):
    return (
        "докум" in getCommand(event)
        or "docum" in getCommand(event)
        or "дакум" in getCommand(event)
        or "декум" in getCommand(event)
        or "дэкум" in getCommand(event)
    ) or isInLastContext(event, 'toAForeignStudent')

def getResponseDocum(event, allDialogs):
    return createResponse(event, getMigrationDocumentsConfig(event))     



def getResponseAdd(event, allDialogs):
    return createResponse(event, getAdditionalOpportsConfig(event))

def isTriggeredAdd(event):
    return (
        "возм" in getCommand(event)
        or "доп" in getCommand(event)
        or "ад" in getCommand(event)
        or "add" in getCommand(event)
    ) or isInLastContext(event, 'toAForeignStudent')



toAForeignStudent = {"getResponse": getResponse, "isTriggered": isTriggered}
toAForeignStudentBench = {"getResponse": getBenchResponse, "isTriggered": isTriggeredBench}
toAForeignStudentAdd = {"getResponse": getResponseAdd, "isTriggered": isTriggeredAdd}
toAForeignStudentDocum = {"getResponse": getResponseDocum, "isTriggered": isTriggeredDocum}
toAForeignStudentMag = {"getResponse": getResponseMag, "isTriggered": isTriggeredMag}
toAForeignStudentInter = {"getResponse": getInterResponse, "isTriggered": isTriggeredInter}
