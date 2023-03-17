from utils.parser.parser import *
from utils.responseHelper import getState

def getConfig(event):
    group = getState(event, "timeTable_group")
    degree = getState(event, 'timeTable_degree')

    message = ""
    tts = ""
    buttons = ["Помощь", "Назад", "Выйти"]

    announces = parser("timetable.getGroupTimetable", [group, degree])
    if not announces:
        message = 'Произошла какая-то ошибка. Скорее всего, вы ввели недействительные данные.'
        tts = 'Произошла какая-то ошибка. Скорее всего, вы ввели недействительные данные.'
        buttons.insert(0, 'Попробовать еще раз')
    else:
        for i in announces:
            message += f"""
            {i['dayWeek']}
            {i['date']}
            {i['hours']}
            {i['whatWeeks']}
            {i['subjectName']}
            {i['lecturerName']}
            {i['classroomNumber']}
            {i['classroomAddress']}
            {i['classroomNavigator']}
            {i['classFormat']}
            ------------
            """
    return {
        "message": message,
        "tts": tts,
        "buttons": buttons
    }