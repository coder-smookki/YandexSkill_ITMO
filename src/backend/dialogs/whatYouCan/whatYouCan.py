from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    return (
        (
            "что" in getCommand(event)
            and (
                "умеешь" in getCommand(event)
                or "можешь" in getCommand(event)
                or "способен" in getCommand(event)
            )
        )
        or (
            "what" in getCommand(event)
            and ("can" in getCommand(event) or "capable" in getCommand(event))
        )
        or (
            "кэн" in getCommand(event)
            or "кен" in getCommand(event)
            or "кан" in getCommand(event)
            or "уат" in getCommand(event)
            or "ват" in getCommand(event)
            or "уэт" in getCommand(event)
            or "вэт" in getCommand(event)
            or "ует" in getCommand(event)
            or "вет" in getCommand(event)
        )
    )


whatYouCan = {"getResponse": getResponse, "isTriggered": isTriggered}
