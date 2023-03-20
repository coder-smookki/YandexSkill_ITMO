askGroupMessage = \
    """
    Напишите вашу группу (например, А1234)
    """

askGroupTts = \
    """
    Продиктуйте вашу группу. Например. А. один, два, три, четыре. Или же. А. тысяча, двести, тридцать, четыре."""

askDegreeMessage = \
    """
    Напишите ваш вид образования (бакалавриат, магистратура, специалитет)
    """

askDegreeTts = \
    """
    Скажите ваш вид образования. Бакалавриат, магистратура, специалитет.
    """

buttons = [
    "Повторить ещё раз",
    'Что ты умеешь?',
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
    elif askSubject == 'degree':
        return {
            'message': askDegreeMessage,
            'tts': askDegreeTts,
            'buttons': buttons,
            'session_state': session_state
        }
