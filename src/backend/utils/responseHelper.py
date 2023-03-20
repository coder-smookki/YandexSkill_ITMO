import copy
from utils.globalStorage import *
from utils.asyncHelper import doFuncAsAsync
from utils.triggerHelper import *
from utils.languageTransliter import replaceNumbersWithWords

def createResponse(event, originalConfig):
    config = copy.deepcopy(originalConfig)

    lang = getLanguage(event)

    returnResponse = {
        "response": {
            "text": config["message"] if "message" in config else "",
            "tts": replaceNumbersWithWords(config["tts"]) if lang == 'ru-RU' else config["tts"],
            "card": config["card"] if "card" in config else None,
            "buttons": createButtons(config["buttons"]),
            "end_session": config["end_session"] if "end_session" in config else False,
        },
        "session": event["session"],
        "session_state": config["session_state"]
        if "session_state" in config
        else {"branch": ""},
        "version": event["version"],
    }
    if "user_state_update" in config:
        returnResponse["user_state_update"] = config["user_state_update"]
    return returnResponse


def createTimeoutResponse(event, allDialogs, getRepsonse, timeoutName):
    lang = getLanguage(event)

    responses = {
        "ru-RU": {
            "loading": {
                "response": {
                    "text": "Загрузка...",
                    "tts": "загрузка",
                    "buttons": createButtons(["Проверить", "Назад", "Выход"]),
                    "end_session": False,
                },
                "session": event["session"],
                "session_state": None,
                "version": event["version"],
            },
            "stillLoading": {
                "response": {
                    "text": "Все еще загрузка...",
                    "tts": "все еще загрузка",
                    "buttons": createButtons(["Проверить", "Назад", "Выход"]),
                    "end_session": False,
                },
                "session": event["session"],
                "session_state": None,
                "version": event["version"],
            }
        },
        "en-US": {
            "loading": {
                "response": {
                    "text": "Loading...",
                    "tts": "loading",
                    "buttons": createButtons(["Check", "Back", "Exit"]),
                    "end_session": False,
                },
                "session": event["session"],
                "session_state": None,
                "version": event["version"],
            },
            "stillLoading": {
                "response": {
                    "text": "Still loading...",
                    "tts": "Still loading",
                    "buttons": createButtons(["Check", "Back", "Exit"]),
                    "end_session": False,
                },
                "session": event["session"],
                "session_state": None,
                "version": event["version"],
            }
        }
    }

    fieldName = timeoutName + "_" + getSessionId(event)
    if not (fieldName in globalStorage):
        setInGlobalStorage(
            fieldName, {"response": "", "isLoaded": False}, overwrite=True
        )

        def getAsyncResponse(event, allDialogs, timeoutName):
            response = getRepsonse(event, allDialogs)
            setInGlobalStorage(
                fieldName, {"response": response, "isLoaded": True}, overwrite=True
            )

        doFuncAsAsync(getAsyncResponse, [event, allDialogs, timeoutName])
        session_state = copy.deepcopy(event["state"]["session"])
        session_state["branch"] = event["state"]["session"]["branch"][-1]
        responses[lang]['loading']['session_state'] = session_state 
        return responses[lang]['loading']

    elif globalStorage[fieldName]["isLoaded"] == False:
        session_state = copy.deepcopy(event["state"]["session"])
        session_state["branch"] = event["state"]["session"]["branch"][-1]
        responses[lang]['loading']['session_state'] = session_state 
        return responses[lang]['stillLoading']

    else:
        response = copy.deepcopy(globalStorage[fieldName]["response"])
        del globalStorage[fieldName]
        return response


def createButtons(buttons):
    result = []
    for button in buttons:
        if isinstance(button, str):
            result.append({"title": button, "hide": True})
            continue
        result.append(button)

    return result


def getSessionId(event):
    return event["session"]["session_id"]


def getUserId(event):
    return event["session"]["user"]["user_id"]


def getState(event, state):
    return event["state"]["session"][state]


def getOriginalUtterance(event):
    return event["request"]["original_utterance"]


def setStateInEvent(event, stateName, stateValue):
    event["state"]["session"][stateName] = stateValue
    return event


def setGlobalStateInEvent(event, stateName, stateValue):
    event["state"]["user"][stateName] = stateValue
    return event


def getCommand(event):
    return event["request"]["command"]


def getGlobalState(event, state):
    return event["state"]["user"][state]


def getLanguage(event):
    allowedLangs = ["ru-RU", "en-US"]
    if haveGlobalState(event, "language"):
        lang = getGlobalState(event, "language")
        if not (lang in allowedLangs):
            lang = "en-US"
    else:
        print("dont have state :(")
        lang = event["meta"]["locale"]
    return lang
