from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()


def getResponse(event, allDialogs=None):
    return createResponse(event, config)


def isTriggered(event):
    token, command = {"бакалавриат"}, "бакалавриат"
    return (
        isSimilarTokens(event, token)
        and isInContext(event, "toAForeignStudent")
        and isSimilarCommand(event, command)
    )


toAForeignStudentBechelorCourse = {
    "getResponse": getResponse,
    "isTriggered": isTriggered,
}
