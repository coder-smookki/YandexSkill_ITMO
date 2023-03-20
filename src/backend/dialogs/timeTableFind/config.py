import re
from utils.responseHelper import *
from utils.parser.parser import *
from math import ceil, floor
from utils.languageTransliter import rusLetterToEng


def getPageConfig(event, pageNum, countOnOnePage):
    words = {
        "ru-RU": {
            "page": "Страница ",
            "pageTo": " из ",
            "dayWeek": "День недели",
            "date": "Дата",
            "hours": "Часы",
            "whatWeeks": "Номера недель",
            "subjectName": "Название предмета",
            "lecturerName": "Лектор",
            "classroomNumber": "Кабинет",
            "classroomAddress": "Адрес",
            "classFormat": "Формат обучения",
            "buttons": [
                "Следующая страница",
                "Предыдущая страница",
                "Повторить ещё раз",
                "Что ты умеешь?",
                "Помощь",
                "Назад",
                "Выйти",
            ],
        },
        "en-US": {
            "page": "Page ",
            "pageTo": " of ",
            "dayWeek": "Day",
            "date": "Date",
            "hours": "Hours",
            "whatWeeks": "Week numbers",
            "subjectName": "Subject",
            "lecturerName": "Lecturer",
            "classroomNumber": "Cabinet",
            "classroomAddress": "Address",
            "classFormat": "Learning format",
            "buttons": [
                "Next page",
                "Previous page",
                "Repeat",
                "What can you do?",
                "Help",
                "Back",
                "Exit",
            ],
        },
    }

    lang = getLanguage(event)
    pages = copy.deepcopy(getState(event, "timeTable_timetable"))
    message = ""
    tts = ""
    
    totalPages = ceil(len(pages) / countOnOnePage)
    if pageNum < 1:
        pageNum = 1
    elif pageNum > totalPages:
        pageNum = totalPages
    lastElem = countOnOnePage * pageNum
    startFromElem = lastElem - countOnOnePage

    message += (
        words[lang]["page"] + str(pageNum) + words[lang]["pageTo"] + str(totalPages)
    )

    # maxPages = len(pages) // pageNum
    for i in pages[startFromElem:lastElem]:
        message += f"""
            {words[lang]["dayWeek"]}: {i['dayWeek']}.
            {words[lang]["date"]}: {i['date']}.
            {words[lang]["hours"]}: {i['hours']}.
            {words[lang]["whatWeeks"]}: {i['whatWeeks']}.
            {words[lang]["subjectName"]}: {i['subjectName']}.
            {words[lang]["lecturerName"]}: {i['lecturerName']}.
            {words[lang]["classroomNumber"]}: {i['classroomNumber']}.
            {words[lang]["classroomAddress"]}: {i['classroomAddress']}.
            {words[lang]["classFormat"]}: {i['classFormat']}.
            ------------
            """
        tts += f"""
            {words[lang]["dayWeek"]}: {i['dayWeek']}.
            {words[lang]["date"]}: {i['date']}.
            {words[lang]["hours"]}: {i['hours']}.
            {words[lang]["subjectName"]}: {i['subjectName']}.
            {words[lang]["lecturerName"]}: {i['lecturerName']}.
            """
    # {i['classroomNavigator']}
    session_state = {
        "branch": "timeTable",
        "timeTable_timetable": pages,
        "timeTable_lastPage": pageNum,
    }

    return {
        "message": message,
        "tts": tts,
        "buttons": words[lang]["buttons"],
        "session_state": session_state,
    }


# [а-яА-Яa-zA-Z\d]+


def getConfig(event, countOnOnePage):
    words = {
        "ru-RU": {
            "buttons": ["Что ты умеешь?", "Помощь", "Назад", "Выйти"],
            "tryAgain": "Произошла какая-то ошибка. Скорее всего, вы ввели недействительные данные.",
            "tryAgainBtn": "Попробовать еще раз",
        },
        "en-US": {
            "buttons": ["What can you do?", "Help", "Back", "Exit"],
            "tryAgain": "Some error has occurred. Most likely, you entered invalid data.",
            "tryAgainBtn": "Try one more time",
        },
    }

    lang = getLanguage(event)

    message = ""
    tts = ""
    buttons = words[lang]["buttons"]

    origGroup = getState(event, "timeTable_group").lower()
    origDegree = getState(event, "timeTable_degree").lower()

    groupLetter = re.findall(r"[а-яА-Яa-zA-Z]+", origGroup)
    groupLetter = "".join(groupLetter)

    groupNums = re.findall(r"\d+", origGroup)
    groupNums = "".join(groupNums)

    group = (rusLetterToEng(groupLetter) + groupNums).upper()

    degree = re.findall(r"[а-яА-Яa-zA-Z]", origDegree)
    degree = "".join(degree)

    timetable = parser("timetable.getGroupTimetable", [group, degree], lang)

    if not timetable:
        message = words[lang]["tryAgain"]
        tts = words[lang]["tryAgain"]
        buttons.insert(0, words[lang]["tryAgainBtn"])
        return {
            "message": message,
            "tts": tts,
            "buttons": buttons,
        }

    else:
        setStateInEvent(event, "timeTable_timetable", timetable)
        setStateInEvent(event, "timeTable_lastPage", 1)
        config = getPageConfig(event, 1, countOnOnePage)

    return config
