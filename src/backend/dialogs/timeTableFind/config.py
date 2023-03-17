from utils.responseHelper import *
from utils.parser.parser import *

def getPageConfig(event, startFromElem, countOnOnePage):
    if not (startFromElem is None) and startFromElem >= 0:
        message = ""
        tts = ""

        pages = copy.deepcopy(getState(event, 'timeTable_timetable'))
        print(len(pages))
        if startFromElem < 0:
            startFromElem = 0
        elif startFromElem > len(pages):
            startFromElem = len(pages) - countOnOnePage

        # maxPages = len(pages) // pageNum
        for i in pages[startFromElem:startFromElem + countOnOnePage]:
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
        lastElem = getState(event, 'timeTable_lastElem')
        session_state = {
            'branch': 'timeTable',
            'timeTable_timetable': pages,
            'timeTable_lastElem': lastElem
        }
        buttons = ["Следующая страница", "Предыдущая страница", "Назад", 'Выйти']
        return {
            "message": message,
            "tts": tts,
            "buttons": buttons,
            'session_state': session_state
        }

def getConfig(event, countOnOnePage):
    group = getState(event, "timeTable_group")
    degree = getState(event, 'timeTable_degree')
    timetable = parser("timetable.getGroupTimetable", [group, degree])
    buttons = ["Помощь", "Назад", "Выйти"]

    if not timetable:
        message = 'Произошла какая-то ошибка. Скорее всего, вы ввели недействительные данные.'
        tts = 'Произошла какая-то ошибка. Скорее всего, вы ввели недействительные данные.'
        buttons.insert(0, 'Попробовать еще раз')
        return {
            "message": message,
            "tts": tts,
            "buttons": buttons,
        }

    else:
        session_state = {
            'branch': 'timeTable',
            'timeTable_timetable': timetable,
            'timeTable_lastElem': 0
        }
        setStateInEvent(event, 'timeTable_timetable', timetable)
        setStateInEvent(event, 'timeTable_lastElem', 0)
        config = getPageConfig(event, 0, countOnOnePage)

    return config