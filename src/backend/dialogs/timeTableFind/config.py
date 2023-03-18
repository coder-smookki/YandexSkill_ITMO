from utils.responseHelper import *
from utils.parser.parser import *
from math import ceil, floor


def getPageConfig(event, pageNum, countOnOnePage):
    pages = copy.deepcopy(getState(event, "timeTable_timetable"))
    message = ""
    tts = ""

    # (1 2 3) (4 5 6) (7)

    # pageNum = 2, countOneOnePage = 3

    lastElem = countOnOnePage * pageNum
    startFromElem = lastElem - countOnOnePage

    message += (
        "Страница "
        + str(floor(startFromElem / countOnOnePage + 1))
        + " из "
        + str(ceil(len(pages) / countOnOnePage))
    )

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
    buttons = ["Следующая страница", "Предыдущая страница", "Назад", "Выйти"]
    return {
        "message": message,
        "tts": tts,
        "buttons": buttons,
        "session_state": session_state,
    }


def getConfig(event, countOnOnePage):
    group = getState(event, "timeTable_group")
    degree = getState(event, "timeTable_degree")
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
        setStateInEvent(event, "timeTable_lastElem", 0)
        config = getPageConfig(event, 0, countOnOnePage)

    return config
