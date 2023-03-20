from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "tts":
            """
    О нас:
    Каждый день у студента возникает миллион вопросов. Как получить справку? Как заменить студенческий билет?
    Возможно ли продлить сессию? На эти и многие другие вопросы знает ответ Студенческий офис.
    Контакты:
    Почта - so, @ itmo, точка, ru.
    Телефон - плюс семь, восемьсот двенадцать, шестьсот семь, ноль четыре, семьдесят четыре. или. Плюс семь, восемьсот двенадцать, четырёхсот восемьдесят, девяносто, два нуля.
    Выберите вопрос чтобы получить ответ:  
    Что такое Студенческий офис?
    Зачем мне обращаться в Студенческий офис?
    Как подать заявку на получение справки/документа о предыдущем образовании?
    Как попасть на консультацию в Студенческий офис?
    Я не знаю, кому задать вопрос. Студенческий офис поможет?
            """,
        "buttons": [
            {
                'title': 'VK',
                'url': 'https://vk.com/student_services_office',
                'hide': False
            },
            {
                'title': 'Telegram',
                'url': 'https://t.me/itmolnia',
                'hide': False
            },
            "Что такое Студенческий офис?",
            "Зачем мне обращаться в Студенческий офис?",
            "Как подать заявку на получение справки/документа о предыдущем образовании?",
            "Как попасть на консультацию в Студенческий офис?",
            "Я не знаю, кому задать вопрос. Студенческий офис поможет?",
            'Что ты умеешь?',
            "Помощь",
            "Назад",
            "Выйти"
        ],

        "card": {
            'type': 'BigImage',
            'image_id': '1521359/65fa68f782fa6af3f071',
            'title': 'СТУДЕНЧЕСКИЙ ОФИС',
            'description': \
                """
                Контакты: Email - so@itmo.ru, Телефон - +7 (812) 607-04-74 или +7 (812) 480-90-00.
                """
        }
    },

    "en-US": {
        "tts":
            """
     About Us:
     Every day a student has a million questions. How to get help? How to replace a student card?
     Is it possible to extend the session? The Student Office knows the answers to these and many other questions.
     Contacts:
     Mail - so@itmo.ru
     Phone - plus seven, eight hundred twelve, six hundred seven, zero four, seventy four. or. Plus seven, eight hundred and twelve, four hundred and eighty, ninety, two zeros.
     Select a question to get an answer:
     What is a Student Office?
     Why should I contact the Student Office?
     How to apply for a certificate/document of previous education?
     How can I get a consultation at the Student Office?
     I don't know who to ask the question. Can the student office help?
            """,
        "buttons": [
            {
                'title': 'VK',
                'url': 'https://vk.com/student_services_office',
                'hide': False
            },
            {
                'title': 'Telegram',
                'url': 'https://t.me/itmolnia',
                'hide': False
            },
            "What is the Student Office?",
            "Why should I contact the Student Office?",
            "How to apply for a certificate/document of previous education?",
            "How to get a consultation at the Student Office?",
            "I don't know who to ask the question."
            "Say it again",
            "What can you do?",
            "Help",
            "Back",
            "Exit",
        ],

        "card": {
            'type': 'BigImage',
             'image_id': '1521359/65fa68f782fa6af3f071',
             'title': 'STUDENT OFFICE',
             'description': \
                 """
                 Mail: so@itmo.ru. Phone: +7 (812) 607-04-74 or +7 (812) 480-90-00..
                 Select a question to get an answer:
                 What is a Student Office?
                 Why should I contact the Student Office?
                 How to apply for a certificate/document of previous education?
                 How can I get a consultation at the Student Office?
                 I don't know who to ask the question. Can the student office help?
                 """
        }
    }
}

session_state = {
    "branch": "studentOffice"
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
