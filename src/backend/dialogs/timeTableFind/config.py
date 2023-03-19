import re
from utils.responseHelper import *
from utils.parser.parser import *
from math import ceil, floor
from utils.languageTransliter import rusLetterToEng


def getPageConfig(event, pageNum, countOnOnePage):
    pages = copy.deepcopy(getState(event, "timeTable_timetable"))
    message = ""
    tts = ""

    # (1 2 3) (4 5 6) (7)

    # pageNum = 2, countOneOnePage = 3
    totalPages = ceil(len(pages) / countOnOnePage)
    if pageNum < 1:
        pageNum = 1
    elif pageNum > totalPages:
        pageNum = totalPages
    lastElem = countOnOnePage * pageNum
    startFromElem = lastElem - countOnOnePage

    message += "Страница " + str(pageNum) + " из " + str(totalPages)

    # maxPages = len(pages) // pageNum
    for i in pages[startFromElem:lastElem]:
        message += f"""
            {i['dayWeek']}
            {i['date']}
            {i['hours']}
            {i['whatWeeks']}
            {i['subjectName']}
            {i['lecturerName']}
            {i['classroomNumber']}
            {i['classroomAddress']}
            {i['classFormat']}
            ------------
            """
    # {i['classroomNavigator']}
    session_state = {
        "branch": "timeTable",
        "timeTable_timetable": pages,
        "timeTable_lastPage": pageNum,
    }
    buttons = ["Следующая страница", "Предыдущая страница", "Помощь", "Назад", "Выйти"]
    return {
        "message": message,
        "tts": tts,
        "buttons": buttons,
        "session_state": session_state,
    }


# [а-яА-Яa-zA-Z\d]+


def getConfig(event, countOnOnePage):
    origGroup = getState(event, "timeTable_group").lower()
    origDegree = getState(event, "timeTable_degree").lower()

    groupLetter = re.findall(r"[а-яА-Яa-zA-Z]+", origGroup)
    groupLetter = "".join(groupLetter)

    groupNums = re.findall(r"\d+", origGroup)
    groupNums = "".join(groupNums)

    group = (rusLetterToEng(groupLetter) + groupNums).upper()

    degree = re.findall(r"[а-яА-Яa-zA-Z]", origDegree)
    degree = "".join(degree)
    print(group)
    print(degree)

    timetable = parser("timetable.getGroupTimetable", [group, degree])
    buttons = ["Помощь", "Назад", "Выйти"]

    if not timetable:
        message = (
            "Произошла какая-то ошибка. Скорее всего, вы ввели недействительные данные."
        )
        tts = (
            "Произошла какая-то ошибка. Скорее всего, вы ввели недействительные данные."
        )
        buttons.insert(0, "Попробовать еще раз")
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
