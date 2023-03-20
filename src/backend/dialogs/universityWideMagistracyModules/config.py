from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "tts": """
            Общеуниверситетские модули это то, с чего начинается обучение в Университете ИТМ+О как в бакалавриате, так и в магистратуре. Это блок фундаментальной подготовки на базе которого студенты приступают к изучению профессиональных дисциплин. Всё продумано: сначала формируются soft skills, необходимые для жизни и работы в условиях цифровой экономики. После этого, в зависимости от образовательной программы и специализации – hard skills.  
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
                "title": "Официальный сайт",
                "url": "https://student.itmo.ru/ru/universitymodules_master/",
                "hide": False,
            },
            "Повторить ещё раз",
            "Что ты умеешь?",
            "Помощь",
            "Назад",
            "Выйти",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "213044/70ec763b4e6221c9bf9a",
            "title": "ОБЩЕУНИВЕРСИТЕТСКИЕ МОДУЛИ В МАГИСТРАТУРЕ",
            "description": """
            Чтобы узнать подробнее, нажмите на кнопку ниже
            """,
        },
    },
    "en-US": {
        "tts": """
            The university-wide modules are what starts education at the University of ITM + O, both in the undergraduate and graduate programs. This is a block of fundamental training on the basis of which students begin to study professional disciplines. Everything is thought out: first, the soft skills necessary for life and work in the digital economy are formed. After that, depending on the educational program and specialization - hard skills.
            List of university-wide modules:
            Applied artificial intelligence.
            Foreign language.
            Entrepreneurial culture or Knowledge-intensive entrepreneurship.
            Soft Skills.
            Thinking.
            Creative technologies.
            To find out more, click on the "Official site" button below the text.
            """,
        "buttons": [
            {
                "title": "Official site",
                "url": "https://student.itmo.ru/en/university_modules_bach/",
                "hide": False,
            },
            "Repeat",
            "What can you do?",
            "Help",
            "Back",
            "Exit",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "213044/70ec763b4e6221c9bf9a",
            "title": "GENERAL UNIVERSITY MODULES IN MASTER STUDIES",
            "description": """
            To find out more, click on the button below
            """,
        },
    },
}

session_state = {"branch": "UniversityWideMagistracyModules"}


def getConfig(event):
    lang = getLanguage(event)
    # lang = "ru-RU"

    return {
        "tts": config[lang]["tts"],
        "buttons": config[lang]["buttons"],
        "card": config[lang]["card"],
        "session_state": session_state,
    }
