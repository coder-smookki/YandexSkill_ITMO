from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *
from utils.globalStorage import *
import copy




def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    return (
        "educ" in getCommand(event)
        or "meth" in getCommand(event)
        or "acad" in getCommand(event)
        or "учеб" in getCommand(event)
        or "едук" in getCommand(event)
        or "эдук" in getCommand(event)
        or "экед" in getCommand(event)
        or "эдэм" in getCommand(event)
        or "акад" in getCommand(event)
        or "акед" in getCommand(event)
        or "акэд" in getCommand(event)
        or "мэф" in getCommand(event)
        or "меф" in getCommand(event)
    ) and (
        "edit" in getCommand(event)
        or "publ" in getCommand(event)
        or "эдит" in getCommand(event)
        or "едит" in getCommand(event)
        or "публ" in getCommand(event)
        or "пабл" in getCommand(event)
        or "побл" in getCommand(event)
    )


educationalPublications = {"getResponse": getResponse, "isTriggered": isTriggered}
