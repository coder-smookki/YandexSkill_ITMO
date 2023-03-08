def general_menu(event, context):
    """
    Точка входа для облачной функции.
    :param event: содержимое request.json().
    :param context: информация о текущем контексте выполнения.
    :return: Ответ будет представлен в виде json автоматически.
    """
    buttons = {
        'suggests': [
            'Русский Язык (Russian Language)',
            'Английский язык (English Language)',
            'Выйти (Exit)',
            'Помощь (Help)'
        ]
    }
    return {
        'response': {
            'text':
                """
Привет Студент! Чтобы пользоваться навыком, выбери язык.

Hello Student! To use the skill, choose a language.

       1. Русский Язык (Russian Language)
       2. Английский Язык (English Language)
                """,
            'tts':
                """
Привет Студент! Чтобы пользоваться навыком, выбери язык.
Hello Student! To use the skill, choose a language.
       Первое - это Русский Язык
       The first is the Russian Language
       Второе - это Английский Язык
       The second is English

                """,
            'card': {
                'type': 'BigImage',
                'image_id': '937455/40f0536e426907808499',
                'title': 'ГЛАВНОЕ МЕНЮ (GENERAL MENU)',
                'description':
                    """
Первое (first) - Рус. Язык (Russian Language)... Второе (second) - Англ. Язык (English Language)...
                """,
            },
            'buttons': [
                {
                    'title': title,
                    'payload': {},
                    'hide': 'true'
                } for title in buttons['suggests']
            ],
            'end': 'false'
        },
        'session': event['session'],
        'version': event['version']
    }


def russian_menu(event, context):
    """
    Точка входа для облачной функции.
    :param event: содержимое request.json().
    :param context: информация о текущем контексте выполнения.
    :return: Ответ будет представлен в виде json автоматически.
    """
    buttons = {
        'suggests': [
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
    }
    return {
        'response': {
            'text':
                """
Ты выбрал Русский Язык! 
Выбери нужную категорию, которая поможет тебе.
1. Новости
2. Студенческий офис
3. Первокурсникам
4. Расписание занятий
5. Расписание сессии
6. Иностранному студенту
7. Общеуниверситетские модули в бакалавриате
8. Общеуниверситетские модули в магистратуре
9. Библиотека
10. Учебные и методические издания
11. Стипендии
12. Задать вопрос
Если такой категории нет, скажите "задать вопрос" и затем заполните всю информацию, чтобы мы могли знать, чего не хватает в навыке.
                """,
            'tts':
                """
Ты выбрал Русский Язык! 
Выбери нужную категорию, которая поможет тебе.
Первое - это Новости.
Второе - это Студенческий офис.
Третье - это Первокурсникам.
Четвёртое - это Расписание занятий.
Пятое - это Расписание сессии.
Шестое - это Иностранному студенту.
Седьмое - это Общеуниверситетские модули в бакалавриате.
Восьмое - это Общеуниверситетские модули в магистратуре.
Девятое - это Библиотека.
Десятое - это Учебные и методические издания.
Одиннадцатое - это Стипендии.
Двенадцатое - это Задать вопрос.
Если такой категории нет, скажите "задать вопрос" и затем заполните всю информацию, чтобы мы могли знать, чего не хватает в навыке.
                """,
            'card': {
                'type': 'BigImage',
                'image_id': '937455/40f0536e426907808499',
                'title': 'КАТАЛОГ',
                'description':
                    """
Ты выбрал Русский Язык! 
Выбери нужную категорию, которая поможет тебе.
1. Новости
2. Студенческий офис
3. Первокурсникам
4. Расписание занятий
5. Расписание сессии
6. Иностранному студенту
7. Общеуниверситетские модули в бакалавриате
8. Общеуниверситетские модули в магистратуре
9. Библиотека
10. Учебные и методические издания
11. Стипендии
12. Задать вопрос
Если такой категории нет, скажите "задать вопрос" и затем заполните всю информацию, чтобы мы могли знать, чего не хватает в навыке.
                """,
            },
            'buttons': [
                {
                    'title': title,
                    'payload': {},
                    'hide': 'true'
                } for title in buttons['suggests']
            ],
            'end': 'false'
        },
        'session': event['session'],
        'version': event['version']
    }


def student_office_menu(event, context):
    """

    :param event: содержимое request.json().
    :param context: информация о текущем контексте выполнения.
    :return: Ответ будет представлен в виде json автоматически.
    """
    buttons = {
        'suggests': [
            '<buttons>'
        ]
    }
    return {
        'response': {
            'text':
                """
Выберите вопрос чтобы получить ответ:

1. Что такое Студенческий офис?
2. Зачем мне обращаться в Студенческий офис?
3. Как подать заявку на получение справки/документа о предыдущем образовании?
4. Как попасть на консультацию в Студенческий офис?
5. Я не знаю, кому задать вопрос. Студенческий офис поможет?
                """,
            'tts':
                """
Выберите вопрос чтобы получить ответ:

1. Что такое Студенческий офис?
2. Зачем мне обращаться в Студенческий офис?
3. Как подать заявку на получение справки/документа о предыдущем образовании?
4. Как попасть на консультацию в Студенческий офис?
5. Я не знаю, кому задать вопрос. Студенческий офис поможет?
                """,
            'card': {
                'type': 'BigImage',
                'image_id': '937455/40f0536e426907808499',
                'title': 'Студенческий офис',
                'description':
                    """
Выберите вопрос чтобы получить ответ:

1. Что такое Студенческий офис?
2. Зачем мне обращаться в Студенческий офис?
3. Как подать заявку на получение справки/документа о предыдущем образовании?
4. Как попасть на консультацию в Студенческий офис?
5. Я не знаю, кому задать вопрос. Студенческий офис поможет?
                """,
            },
            'buttons': [
                {
                    'title': title,
                    'payload': {},
                    'hide': 'true'
                } for title in buttons['suggests']
            ],
            'end': 'false'
        },
        'session': event['session'],
        'session_state': {
            'branch': 'student_office'
        },
        'version': event['version']
    }


def for_freshmen(event, context):
    """

    :param event: содержимое request.json().
    :param context: информация о текущем контексте выполнения.
    :return: Ответ будет представлен в виде json автоматически.
    """
    buttons = {
        "suggests": [

        ]
    }
    return {
        'response': {
            'text':
                """
                """,
            'tts':
                """
                """,
            'card': {
                'type': 'BigImage',
                'image_id': '937455/40f0536e426907808499',
                'title': '',
                'description':
                    """
                    """,
            },
            'buttons': [
                {
                    'title': title,
                    'payload': {},
                    'hide': 'true'
                } for title in buttons['suggests']
            ],
            'end': 'false'
        },
        'session': event['session'],
        'session_state': {
            'branch': 'for_freshmen'  # !
        },
        'version': event['version']
    }


def class_timetable_start(event, context):
    """
    Окно с текстом "Вы выбрали категорию расписание уроков", поэтому _start

    :param event: содержимое request.json().
    :param context: информация о текущем контексте выполнения.
    :return: Ответ будет представлен в виде json автоматически.
    """
    buttons = {
        "suggests": [

        ]
    }
    return {
        'response': {
            'text':
                """
                """,
            'tts':
                """
                """,
            'card': {
                'type': 'BigImage',
                'image_id': '937455/40f0536e426907808499',
                'title': '',
                'description':
                    """
                    """,
            },
            'buttons': [
                {
                    'title': title,
                    'payload': {},
                    'hide': 'true'
                } for title in buttons['suggests']
            ],
            'end': 'false'
        },
        'session': event['session'],
        'session_state': {
            'branch': 'class_schedule_start'  # !
        },
        'version': event['version']
    }


def session_timetable(event, context):
    """
    Окно с текстом "Вы выбрали категорию расписание сессии", поэтому _start

    :param event: содержимое request.json().
    :param context: информация о текущем контексте выполнения.
    :return: Ответ будет представлен в виде json автоматически.
    """
    buttons = {
        "suggests": [

        ]
    }
    return {
        'response': {
            'text':
                """
                """,
            'tts':
                """
                """,
            'card': {
                'type': 'BigImage',
                'image_id': '937455/40f0536e426907808499',
                'title': '',
                'description':
                    """
                    """,
            },
            'buttons': [
                {
                    'title': title,
                    'payload': {},
                    'hide': 'true'
                } for title in buttons['suggests']
            ],
            'end': 'false'
        },
        'session': event['session'],
        'session_state': {
            'branch': 'session_schedule_start'  # !
        },
        'version': event['version']
    }


def for_international_students_start(event, context):
    """
    Окно с текстом "Вы выбрали категорию для иностранных студентов", поэтому _start, т.к. дальше выбор вопросов
    Можно поменять _start на _category

    :param event: содержимое request.json().
    :param context: информация о текущем контексте выполнения.
    :return: Ответ будет представлен в виде json автоматически.
    """
    buttons = {
        "suggests": [

        ]
    }
    return {
        'response': {
            'text':
                """
                """,
            'tts':
                """
                """,
            'card': {
                'type': 'BigImage',
                'image_id': '937455/40f0536e426907808499',
                'title': '',
                'description':
                    """
                    """,
            },
            'buttons': [
                {
                    'title': title,
                    'payload': {},
                    'hide': 'true'
                } for title in buttons['suggests']
            ],
            'end': 'false'
        },
        'session': event['session'],
        'session_state': {
            'branch': 'for_international_students_start'  # !
        },
        'version': event['version']
    }


def university_wide_modules_in_the_bachelors_degree(event, context):
    """

    :param event: содержимое request.json().
    :param context: информация о текущем контексте выполнения.
    :return: Ответ будет представлен в виде json автоматически.
    """
    buttons = {
        "suggests": [

        ]
    }
    return {
        'response': {
            'text':
                """
                """,
            'tts':
                """
                """,
            'card': {
                'type': 'BigImage',
                'image_id': '937455/40f0536e426907808499',
                'title': '',
                'description':
                    """
                    """,
            },
            'buttons': [
                {
                    'title': title,
                    'payload': {},
                    'hide': 'true'
                } for title in buttons['suggests']
            ],
            'end': 'false'
        },
        'session': event['session'],
        'session_state': {
            'branch': 'university_wide_modules_in_the_bachelors_degree'  # !
        },
        'version': event['version']
    }


def university_wide_modules_in_the_masters_degree(event, context):
    """

    :param event: содержимое request.json().
    :param context: информация о текущем контексте выполнения.
    :return: Ответ будет представлен в виде json автоматически.
    """
    buttons = {
        "suggests": [

        ]
    }
    return {
        'response': {
            'text':
                """
                """,
            'tts':
                """
                """,
            'card': {
                'type': 'BigImage',
                'image_id': '937455/40f0536e426907808499',
                'title': '',
                'description':
                    """
                    """,
            },
            'buttons': [
                {
                    'title': title,
                    'payload': {},
                    'hide': 'true'
                } for title in buttons['suggests']
            ],
            'end': 'false'
        },
        'session': event['session'],
        'session_state': {
            'branch': 'university_wide_modules_in_the_masters_degree'  # !
        },
        'version': event['version']
    }


def library_category(event, context):
    """
    _category для прикола добавил, в состоянии сессии нету)

    :param event: содержимое request.json().
    :param context: информация о текущем контексте выполнения.
    :return: Ответ будет представлен в виде json автоматически.
    """
    buttons = {
        "suggests": [

        ]
    }
    return {
        'response': {
            'text':
                """
                """,
            'tts':
                """
                """,
            'card': {
                'type': 'BigImage',
                'image_id': '937455/40f0536e426907808499',
                'title': '',
                'description':
                    """
                    """,
            },
            'buttons': [
                {
                    'title': title,
                    'payload': {},
                    'hide': 'true'
                } for title in buttons['suggests']
            ],
            'end': 'false'
        },
        'session': event['session'],
        'session_state': {
            'branch': 'library'  # !
        },
        'version': event['version']
    }


def educational_and_methodological_publications(event, context):
    """

    :param event: содержимое request.json().
    :param context: информация о текущем контексте выполнения.
    :return: Ответ будет представлен в виде json автоматически.
    """
    buttons = {
        "suggests": [

        ]
    }
    return {
        'response': {
            'text':
                """
                """,
            'tts':
                """
                """,
            'card': {
                'type': 'BigImage',
                'image_id': '937455/40f0536e426907808499',
                'title': '',
                'description':
                    """
                    """,
            },
            'buttons': [
                {
                    'title': title,
                    'payload': {},
                    'hide': 'true'
                } for title in buttons['suggests']
            ],
            'end': 'false'
        },
        'session': event['session'],
        'session_state': {
            'branch': 'educational_and_methodological_publications'  # !
        },
        'version': event['version']
    }


def scholarships(event, context):
    """

    :param event: содержимое request.json().
    :param context: информация о текущем контексте выполнения.
    :return: Ответ будет представлен в виде json автоматически.
    """
    buttons = {
        "suggests": [

        ]
    }
    return {
        'response': {
            'text':
                """
                """,
            'tts':
                """
                """,
            'card': {
                'type': 'BigImage',
                'image_id': '937455/40f0536e426907808499',
                'title': '',
                'description':
                    """
                    """,
            },
            'buttons': [
                {
                    'title': title,
                    'payload': {},
                    'hide': 'true'
                } for title in buttons['suggests']
            ],
            'end': 'false'
        },
        'session': event['session'],
        'session_state': {
            'branch': 'scholarships'  # !
        },
        'version': event['version']
    }


def ask_a_question_start(event, context):
    """
    Окно с текстом "Вы направились в категорию "Задать вопрос", поэтому _start
    Можно сменить на что-то, как запрос ФИО.

    :param event: содержимое request.json().
    :param context: информация о текущем контексте выполнения.
    :return: Ответ будет представлен в виде json автоматически.
    """
    buttons = {
        "suggests": [

        ]
    }
    return {
        'response': {
            'text':
                """
                """,
            'tts':
                """
                """,
            'card': {
                'type': 'BigImage',
                'image_id': '937455/40f0536e426907808499',
                'title': '',
                'description':
                    """
                    """,
            },
            'buttons': [
                {
                    'title': title,
                    'payload': {},
                    'hide': 'true'
                } for title in buttons['suggests']
            ],
            'end': 'false'
        },
        'session': event['session'],
        'session_state': {
            'branch': 'ask_a_question_start'  # !
        },
        'version': event['version']
    }


def news_category(event, context):
    """
    _category для прикола добавил, в состоянии сессии нету)

    :param event: содержимое request.json().
    :param context: информация о текущем контексте выполнения.
    :return: Ответ будет представлен в виде json автоматически.
    """
    buttons = {
        "suggests": [

        ]
    }
    return {
        'response': {
            'text':
                """
                """,
            'tts':
                """
                """,
            'card': {
                'type': 'BigImage',
                'image_id': '937455/40f0536e426907808499',
                'title': '',
                'description':
                    """
                    """,
            },
            'buttons': [
                {
                    'title': title,
                    'payload': {},
                    'hide': 'true'
                } for title in buttons['suggests']
            ],
            'end': 'false'
        },
        'session': event['session'],
        'session_state': {
            'branch': 'news'
        },
        'version': event['version']
    }
