from .config import getConfig
from utils.triggerHelper import *
from utils.responseHelper import *
from utils.branchHandler import getDialogResponseFromEnd

config = getConfig()


def getResponse(event, allDialogs=None):
    print("exitConfirm")
    if isInContext(event, "exitConfirm") and (
        "да" in getCommand(event)
        or "конечно" in getCommand(event)
        or "уверен" in getCommand(event)
        or "точно" in getCommand(event)
        or "выйти" in getCommand(event)
        or "выход" in getCommand(event)
        or "выйди" in getCommand(event)
    ):
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
                or "yes" in getCommand(event)
                or "sure" in getCommand(event)
                or "йес" in getCommand(event)
                or "иес" in getCommand(event)
                or "йез" in getCommand(event)
                or "иез" in getCommand(event)
                or "шур" in getCommand(event)
                or "сюр" in getCommand(event)
                or "шьюр" in getCommand(event)
                or "сьюр" in getCommand(event)
            )
        )
        or "exit" in getCommand(event)
        or "выйти" in getCommand(event)
        or "выход" in getCommand(event)
        or "выйди" in getCommand(event)
        or "экзит" in getCommand(event)
        or "екзит" in getCommand(event)
        or "эксит" in getCommand(event)
        or "ексит" in getCommand(event)
        or "close" in getCommand(event)
        or "клоз" in getCommand(event)
        or "клоуз" in getCommand(event)
        or "клос" in getCommand(event)
        or "клоус" in getCommand(event)
    )


exitConfirm = {"getResponse": getResponse, "isTriggered": isTriggered}
