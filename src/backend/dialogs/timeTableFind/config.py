from utils.responseHelper import *
from utils.parser.parser import *

def getConfig(event, startFromElem=None):
    message = ""
    tts = ""

    if not (startFromElem is None) and startFromElem >= 0:
        countOnOnePage = 3
        pages = copy.deepcopy(getState(event, 'timeTable_timetable'))
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
            {i['classroomNavigator']}
            {i['classFormat']}
            ------------
            """
        # {i['classroomAddress']}

        session_state = {
            'branch': 'timeTable',
            'timeTable_timetable': pages
        }
        buttons = ["Следующая страница", "Предыдущая страница", "Назад", 'Выйти']
        print(message)
        return {
            "message": message,
            "tts": tts,
            "buttons": buttons,
            'session_state': session_state
        }

    group = getState(event, "timeTable_group")
    degree = getState(event, 'timeTable_degree')
    timetable = parser("timetable.getGroupTimetable", [group, degree])
    buttons = ["Помощь", "Назад", "Выйти"]

    if not timetable:
        message = 'Произошла какая-то ошибка. Скорее всего, вы ввели недействительные данные.'
        tts = 'Произошла какая-то ошибка. Скорее всего, вы ввели недействительные данные.'
        buttons.insert(0, 'Попробовать еще раз')
        session_state = {
            'branch': 'timeTable',
            'timeTable_timetable': timetable,
            'timeTable_lastPage': 0
        }
        setStateInEvent(event, 'timeTable_timetable', timetable)
        setStateInEvent(event, 'timeTable_lastPage', 0)
    else:
        return getConfig(event, 0)
    return {
        "message": message,
        "tts": tts,
        "buttons": buttons,
        'session_state': session_state
    }