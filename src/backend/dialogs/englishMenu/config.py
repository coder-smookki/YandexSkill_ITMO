message = \
    """
    You chose English language! 
    Choose the right category that will help you.
    1. News
    2. Student Office
    3. For freshmen
    4. Class schedule
    5. Session schedule
    6. For international students
    7. University-wide modules in the Bachelor's degree
    8. University-wide modules in the Master's program
    9. Library
    10. Educational and methodological publications
    11. Scholarships
    12. Ask a question
    If there is no such category, say "ask a question" and then fill in all the information so that we can know what is missing in the skill.
    """
 
tts = \
    """
    You chose English language! 
    Choose the right category that will help you.
    1. News
    2. Student Office
    3. For freshmen
    4. Class schedule
    5. Session schedule
    6. For international students
    7. University-wide modules in the Bachelor's degree
    8. University-wide modules in the Master's program
    9. Library
    10. Educational and methodological publications
    11. Scholarships
    12. Ask a question
    If there is no such category, say "ask a question" and then fill in all the information so that we can know what is missing in the skill.
    """

buttons = [
    {
        'title': 'test',
        'url': 'https://google.com',
        'hide': True
    },
    'Новости',
    'Студенческий офис',
    'Первокурсникам',
    'Расписание занятий',
    'Расписание сессии',
    'Иностранному студенту',
    'Общеуниверситетские модули в бакалавриате',
    'Общеуниверситетские модули в магистратуре',
    'Библиотека',
    'Учебные и методические издания',
    'Стипендии',
    'Задать вопрос',
    'Помощь',
    'Назад',
    'Выйти'
]

card = {
    'type': 'BigImage',
    'image_id': '937455/40f0536e426907808499',
    'title': 'КАТАЛОГ',
    'description':
        """
        You chose English language! 
        Choose the right category that will help you.
        1. News
        2. Student Office
        3. For freshmen
        4. Class schedule
        5. Session schedule
        6. For international students
        7. University-wide modules in the Bachelor's degree
        8. University-wide modules in the Master's program
        9. Library
        10. Educational and methodological publications
        11. Scholarships
        12. Ask a question
        If there is no such category, say "ask a question" and then fill in all the information so that we can know what is missing in the skill.
        """
}

session_state = {
    "branch_2": "generalMenu"
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }
