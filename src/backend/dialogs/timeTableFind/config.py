from utils.parser.parser import *
from utils.responseHelper import getState


def getConfig(event):


    group = getState(event, "timeTable_group")
    degree = getState(event, 'timeTable_degree')

    print(group)
    print(degree)

    message = ""
    tts = ""
    buttons = ["Помощь", "Назад", "Выйти"]

    announces = parser("timetable.getGroupTimetable", [group, degree])
    if not announces:
        message='Произошла какая-то ошибка. Скорее всего, вы ввели недействительные данные.'
        tts = 'Произошла какая-то ошибка. Скорее всего, вы ввели недействительные данные.'
        buttons.insert(0, 'Попробовать еще раз')
    else:
        for i in announces:
            message += f"""
            {i['dayWeek']}\n
            {i['date']}\n
            {i['hours']}\n
            {i['whatWeeks']}\n
            {i['subjectName']}\n
            {i['lecturerName']}\n
            {i['classroomNumber']}\n
            {i['classroomAddress']}\n
            {i['classroomNavigator']}\n
            {i['classFormat']}\n
            ------------\n
            """

    return {
        "message": message,
        "tts": tts,
        "buttons": buttons,
    }
