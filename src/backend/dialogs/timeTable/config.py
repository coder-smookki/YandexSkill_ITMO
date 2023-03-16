askGroupMessage = \
    """
    Напишите вашу группу (например, А1234)
    """

askGroupTts = \
    """
    Продиктуйте вашу Группу (например, А1234)
    """

askCourseMessage = \
    """
    Напишите номер вашего Курса
    """

askCourseTts = \
    """
    Продиктуйте номер вашего Курса
    """

buttons = [
    "Повторить ещё раз",
    "Помощь",
    "Назад",
    "Выйти"
]

session_state = {
    "branch": "timeTable"
}


def getConfig(askSubject):
    if askSubject == 'group': 
        return {
            'message': askGroupMessage,
            'tts': askGroupTts,
            'buttons': buttons,
            'session_state': session_state
        }
    elif askSubject == 'course':
        return {
            'message': askCourseMessage,
            'tts': askCourseTts,
            'buttons': buttons,
            'session_state': session_state
        }