from .config import getConfig
from utils.triggerHelper import *
from utils.responseHelper import *
from utils.branchHandler import getDialogResponseFromEnd

config = getConfig()


def getResponse(event, allDialogs=None):
    print("exitConfirm")
    if isInContext(event, "exitConfirm") and isSimilarCommand(event, "да"):
        response = {
            "response": {
                "text": "До скорых встреч! Были рады вас видеть в нашем навыке!",
                "tts": "До скорых встреч! Были рады вас видеть в нашем навыке!",
                "buttons": [],
                "end_session": True,
            },
            "version": event["version"],
            "dontUpdateBranches": True,
        }
        return response
    elif isInContext(event, "exitConfirm"):
        return getDialogResponseFromEnd(event, 2, allDialogs)
    return createResponse(event, config)


def isTriggered(event):
    return (
        (
            isInContext(event, "exitConfirm")
            and (
                "да" in getCommand(event)
                or "конечно" in getCommand(event)
                or "уверен" in getCommand(event)
                or "точно" in getCommand(event)
                or "выйти" in getCommand(event)
                or "выход" in getCommand(event)
                or "выйди" in getCommand(event)
            )
        )
        or "выйти" in getCommand(event)
        or "выход" in getCommand(event)
        or "выйди" in getCommand(event)
        or isSimilarCommand(event, "все")
        or isSimilarCommand(event, "всё")
    )


exitConfirm = {"getResponse": getResponse, "isTriggered": isTriggered}
