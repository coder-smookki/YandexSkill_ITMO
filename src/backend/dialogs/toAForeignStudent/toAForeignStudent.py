from .config import *
from utils.responseHelper import *
from utils.triggerHelper import *
from utils.branchHandler import getDialogResponseFromEnd


def getResponse(event, allDialogs=None):
    if not isInLastContext(event, "toAForeignStudent"):
        return createResponse(event, getMainConfig(event))

    if (
        "бакал" in getCommand(event)
        or "benc" in getCommand(event)
        or "banc" in getCommand(event)
        or "бэнч" in getCommand(event)
        or "банч" in getCommand(event)
    ):
        return createResponse(event, getBechelorConfig(event))

    if (
        "между" in getCommand(event)
        or "народ" in getCommand(event)
        or "inter" in getCommand(event)
        or "интер" in getCommand(event)
        or "nation" in getCommand(event)
    ) and (
        "магис" in getCommand(event)
        or "mast" in getCommand(event)
        or "magic" in getCommand(event)
        or "мег" in getCommand(event)
        or "мэг" in getCommand(event)
        or "mast" in getCommand(event)
        or "маст" in getCommand(event)
        or "маг" in getCommand(event)
    ):
        return createResponse(event, getInternationalMagistracyConfig(event))

    if (
        "магис" in getCommand(event)
        or "magic" in getCommand(event)
        or "mast" in getCommand(event)
        or "маст" in getCommand(event)
        or "мег" in getCommand(event)
        or "мэг" in getCommand(event)
        or "маг" in getCommand(event)
    ):
        return createResponse(event, getMagistracyConfig(event))

    if (
        "докум" in getCommand(event)
        or "docum" in getCommand(event)
        or "дакум" in getCommand(event)
        or "декум" in getCommand(event)
        or "дэкум" in getCommand(event)
    ):
        return createResponse(event, getMigrationDocumentsConfig(event))

    if (
        "возм" in getCommand(event)
        or "доп" in getCommand(event)
        or "ад" in getCommand(event)
        or "add" in getCommand(event)
    ):
        return createResponse(event, getAdditionalOpportsConfig(event))

    return createResponse(event, getMainConfig(event))


def isTriggered(event):
    return isInLastContext(event, "toAForeignStudent") or (
        (
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
        )
        and isInContext(event, "mainMenu")
    )


toAForeignStudent = {"getResponse": getResponse, "isTriggered": isTriggered}
