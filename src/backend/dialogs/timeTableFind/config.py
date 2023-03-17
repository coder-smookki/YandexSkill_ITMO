from utils.responseHelper import *
from utils.parser.parser import *

def getConfig(event, startFromElem=None, countOnOnePage=3):
    message = ""
    tts = ""

    if not (startFromElem is None) and startFromElem >= 0:
        pages = getState(event, 'timeTable_timetable')

        if startFromElem < 0:
            startFromElem = 0
        elif startFromElem > len(pages):
            startFromElem = len(pages) - countOnOnePage

        # maxPages = len(pages) // pageNum
        for i in pages[startFromElem:startFromElem + countOnOnePage + 1]:
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
            'timeTable_timetable': pages,
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
    else:
        session_state = {
            'branch': 'timeTable',
            'timeTable_timetable': timetable,
            'timeTable_lastElem': 0
        }
        setStateInEvent(event, 'timeTable_timetable', timetable)
        setStateInEvent(event, 'timeTable_lastElem', 0)
        config = getConfig(event, 0)
    return config