from utils.parser.parser import *
from utils.responseHelper import getState

buttons = ["Помощь", "Назад", "Выйти"]

session_state = {"branch": "timeTable"}


def getConfig(event):
    group = getState(event, "timeTable_group")
    course = int(getState(event, "timeTable_course"))
    message = ""
    tts = ""

    announces = parser("timetable.getGroupTimetable", [group, course])

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
        "session_state": session_state,
    }
