from utils.responseHelper import getGlobalState, getLanguage

tts = \
    """
    Учеба идет проще, когда тебя хвалят, именно поэтому в Университете ИТМО существуют разные стипендиальные выплаты. Они нацелены на стимулирование и поддержку студентов во время обучения.
    Существует множество видов стипендиальных выплат:
    Государственная академическая стипендия;
    Повышенная государственная академическая стипендия;
    Государственная стипендия аспирантам, ординаторам, ассистентам-стажерам;
    Государственная социальная стипендия;
    Материальная поддержка студентам и аспирантам;
    Стипендия Президента РФ и Правительства РФ;
    Конкурс стипендий Президента РФ для обучения за рубежом;
    Именная стипендия Правительства Санкт-Петербурга;
    Стипендия «Альфа-Шанс»;
    Стипендия фонда Владимира Потанина.
    Есть вопросы? Задайте их Стипендиальной комиссии!
    """

config = {
    "ru-RU": {
        "tts":
            """
            Вы направились в категорию "Стипендии".
        Учеба идет проще, когда тебя хвалят, именно поэтому в Университете ИТМО существуют разные стипендиальные выплаты. Они нацелены на стимулирование и поддержку студентов во время обучения.
        Существует множество видов стипендиальных выплат:
        Государственная академическая стипендия;
        Повышенная государственная академическая стипендия;
        Государственная стипендия аспирантам, ординаторам, ассистентам-стажёрам;
        Государственная социальная стипендия;
        Материальная поддержка студентам и аспирантам;
        Стипендия Президента РФ и Правительства РФ;
        Конкурс стипендий Президента РФ для обучения за рубежом;
        Именная стипендия Правительства Санкт-Петербурга;
        Стипендия «Альфа-Шанс»;
        Стипендия фонда Владимира Потанина.
        Есть вопросы? - Задайте их Стипендиальной комиссии!
            """,
        "buttons": [
            {
                'title': 'Сайт стипендии',
                'url': 'https://student.itmo.ru/ru/scholarship/',
                'hide': False
            },
            'Повторить ещё раз',
            'Что ты умеешь?',
            'Помощь',
            'Назад',
            'Выйти'
        ],

        "card": {
            'type': 'BigImage',
            'image_id': '1533899/b86b0073c0e88e67d092',
            'title': 'СТИПЕНДИИ',
            'description':
                """
                Есть вопросы? Задайте их Стипендиальной комиссии! Почта - ursi@itmo.ru
                """
        }
    },

    "en-US": {
        "tts":
            """
            You are headed to the "Scholarships" category.
     Studying is easier when you are praised, which is why ITMO University offers different scholarships. They are aimed at stimulating and supporting students during their studies.
     There are many types of scholarships:
     State academic scholarship;
     Increased state academic scholarship;
     State scholarship for graduate students, residents, assistant trainees;
     State social scholarship;
     Financial support for students and graduate students;
     Scholarship of the President of the Russian Federation and the Government of the Russian Federation;
     Competition of scholarships of the President of the Russian Federation for studying abroad;
     Personal scholarship of the Government of St. Petersburg;
     Scholarship "Alfa-Chance";
     Vladimir Potanin Foundation Scholarship.
     Have questions? Ask them to the Scholarship Commission!
            """,
        "buttons": [
            {
                'title': 'Scholarship Site',
                'url': 'https://student.itmo.ru/en/scholarship/',
                'hide': False
            },
            'Repeat one more time',
            'What can you do?',
            'Help',
            'Back',
            'Go out'
        ],

        "card": {
            'type': 'BigImage',
            'image_id': '1533899/b86b0073c0e88e67d092',
            'title': 'SCHOLARSHIPS',
            'description':
                """
                Have questions? Ask them to the Scholarship Commission! Mail - ursi@itmo.ru
                """
        }
    }
}

session_state = {
    "branch": "scholarships"
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
