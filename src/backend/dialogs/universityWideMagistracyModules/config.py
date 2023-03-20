from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "tts":
            """
    Общеуниверситетские модули – то, с чего начинается обучение в Университете ИТМО как в бакалавриате, так и в магистратуре. Это блок фундаментальной подготовки, на базе которого студенты приступают к изучению профессиональных дисциплин. Всё продумано: сначала формируются soft skills, необходимые для жизни и работы в условиях цифровой экономики, после этого, в зависимости от образовательной программы и специализации – hard skills.  
    Список общеуниверситетских модулей:
    Прикладной искусственный интеллект.
    Иностранный язык.
    Предпринимательская культура или Наукоёмкое предпринимательство.
    Soft Skills.
    Мышление.
    Креативные технологии.
    Чтобы узнать подробнее, нажмите под текстом на кнопку "Официальный сайт".
            """,
        "buttons": [
            {
                'title': 'Официальный сайт',
                'url': 'https://student.itmo.ru/ru/universitymodules_master/',
                'hide': False
            },
            "Повторить ещё раз",
            'Что ты умеешь?',
            "Помощь",
            "Назад",
            "Выйти",
        ],

        "card": {
            'type': 'BigImage',
            'image_id': '213044/70ec763b4e6221c9bf9a',
            'title': 'ОБЩЕУНИВЕРСИТЕТСКИЕ МОДУЛИ В МАГИСТРАТУРЕ',
            'description': \
                """
                Чтобы узнать подробнее, перейдите по ссылке - https://student.itmo.ru/ru/university_modules_bach/
                """
        }
    },

    "en-US": {
        "tts":
            """
            You have been directed to the category "University undergraduate modules".
    University-wide modules are the starting point for studying at ITMO University for both undergraduate and graduate programs. This is a block of fundamental training, on the basis of which students begin to study professional disciplines. Everything is thought out: first, soft skills are formed that are necessary for life and work in a digital economy, after that, depending on the educational program and specialization, hard skills.
    List of university-wide modules:
    The first is digital culture.
    The second is Entrepreneurial Culture and Technological Entrepreneurship.
    Third - Foreign language, first course.
    Fourth - Foreign language, from the second to the fourth year.
    Fifth - Soft Skills.
    And the sixth is thinking.
            """,
        "buttons": [
            {
                'title': 'Official site',
                'url': 'https://student.itmo.ru/en/university_modules_bach/',
                'hide': False
            },
            "Repeat one more time",
            'What can you do?',
            "Help",
            "Back",
            "Exit",
        ],

        "card": {
            'type': 'BigImage',
            'image_id': '937455/40f0536e426907808499',
            'title': 'UNIVERSITY GENERAL MODULES IN BACHELORS',
            'description': \
                """
                You can find out more on the website
                """
        }
    }
}

session_state = {
    "branch": "UniversityWideMagistracyModules"
}


def getConfig(event):
    lang = getLanguage(event)
    # lang = "ru-RU"

    return {
        "tts": config[lang]["tts"],
        "buttons": config[lang]["buttons"],
        "card": config[lang]["card"],
        "session_state": session_state,
    }
