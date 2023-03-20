from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    return (
        "новост" in getCommand(event)
        or 'вест' in getCommand(event)
        or "ньюс" in getCommand(event)
        or "нюс" in getCommand(event)
        or "нус" in getCommand(event)
        or "ниус" in getCommand(event)
        or "ньус" in getCommand(event)
        or "ньос" in getCommand(event)
        or "news" in getCommand(event)
    ) and isInLastContext(event, "mainMenu")


news = {"getResponse": getResponse, "isTriggered": isTriggered}
