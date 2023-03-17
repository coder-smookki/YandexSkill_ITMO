from utils.responseHelper import *
from utils.parser.parser import *

def getConfig(event, pageNum=None):
    message = ""
    tts = ""

    if not (pageNum is None) and pageNum >= 1:
        countOnOnePage = 3
        startPagesArrFrom = (pageNum - 1) * countOnOnePage
        pages = copy.deepcopy(getState(event, 'timeTable_timetable'))
        # maxPages = len(pages) // pageNum
        if startPagesArrFrom >= len(pages):
            startPagesArrFrom = len(pages) - (len(pages)-1) % countOnOnePage
            if startPagesArrFrom == len(pages):
                startPagesArrFrom = (len(pages)-1) - 3
        for i in pages[pageNum:startPagesArrFrom + countOnOnePage]:
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

    session_state = {
        'branch': 'timeTable',
        'timeTable_timetable': timetable
    }
    setStateInEvent(event, 'timeTable_timetable', timetable)

    if not timetable:
        message = 'Произошла какая-то ошибка. Скорее всего, вы ввели недействительные данные.'
        tts = 'Произошла какая-то ошибка. Скорее всего, вы ввели недействительные данные.'
        buttons.insert(0, 'Попробовать еще раз')
    else:
        return getConfig(event, 1)
    return {
        "message": message,
        "tts": tts,
        "buttons": buttons,
        'session_state': session_state
    }