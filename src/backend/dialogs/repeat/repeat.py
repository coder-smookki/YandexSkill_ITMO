from utils.triggerHelper import *
from utils.responseHelper import *
from utils.branchHandler import getDialogResponseFromEnd


def getResponse(event, allDialogs=None):
    return allDialogs[getState(event, "branch")[-1]]["getResponse"](event, allDialogs)


def isTriggered(event):
    return (
        "повтори" in getCommand(event)
        or "еще раз" in getCommand(event)
        or "ещё раз" in getCommand(event)
        or (
            (
                "say" in getCommand(event)
                or "сэй" in getCommand(event)
                or "сей" in getCommand(event)
                or "сай" in getCommand(event)
            )
            and (
                "again" in getCommand(event)
                or "эгеин" in getCommand(event)
                or "эгэин" in getCommand(event)
                or "игэин" in getCommand(event)
                or "игеин" in getCommand(event)
                or "егеин" in getCommand(event)
                or "егэин" in getCommand(event)
                or "эгеен" in getCommand(event)
                or "эгэен" in getCommand(event)
                or "игэен" in getCommand(event)
                or "игеен" in getCommand(event)
                or "егеен" in getCommand(event)
                or "егэен" in getCommand(event)
                or "эгеэн" in getCommand(event)
                or "эгээн" in getCommand(event)
                or "игээн" in getCommand(event)
                or "игеэн" in getCommand(event)
                or "егеэн" in getCommand(event)
                or "егээн" in getCommand(event)
                or "эген" in getCommand(event)
                or "эгэн" in getCommand(event)
                or "игэн" in getCommand(event)
                or "иген" in getCommand(event)
                or "еген" in getCommand(event)
                or "егэн" in getCommand(event)
            )
        )
        or "repeat" in getCommand(event)
        or "репит" in getCommand(event)
        or "рэпит" in getCommand(event)
        or "рэпет" in getCommand(event)
        or "репет" in getCommand(event)
        or "рипит" in getCommand(event)
        or "рипет" in getCommand(event)
        or "рипэт" in getCommand(event)
    )


repeat = {"getResponse": getResponse, "isTriggered": isTriggered}
