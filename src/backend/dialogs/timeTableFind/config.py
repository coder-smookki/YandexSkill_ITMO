from utils.parser.parser import *

buttons = [
    "Назад",
    "Выйти",
    "Помощь"
]

session_state = {
    "branch": "timeTable"
}

def getConfig(event):
    message = ''
    tts = ''

    announces = parser('timetable.getGroupTimetable', [event["request"]['command'].split()[0], int(event["request"]['command'].split()[1])])

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
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'session_state': session_state
    }