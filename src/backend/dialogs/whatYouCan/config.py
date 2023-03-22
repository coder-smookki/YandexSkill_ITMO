from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "tts": """
        С помощью навыка можно узнать последние новости из жизни университета, получить информацию о расписании занятий, узнать некоторые важные аспекты учебного процесса.
        Для удобства первокурсников в навыке есть специальный раздел, где можно найти полезные советы и информацию о том, как успешно начать свой путь в университете. 
        Кроме того, "ИТМО помощник" предоставляет информацию о предметах, которые необходимо изучить в рамках бакалавриата и магистратуры, а также о доступных стипендиях и грантах для студентов.
        Для любителей настольных игр в навыке есть возможность сыграть партию шахмат, а для желающих проверить свои знания - интересные викторины и случайные факты об окружающем мире и ИТМО. 
        Кроме того, в "ИТМО помощнике" можно найти учебные материалы и методические пособия.
        Также для иностранных студентов есть поддержка английского языка.
        """,
        "buttons": ["Повторить ещё раз", "Помощь", "Назад", "Выйти"],
        "card": {
            "type": "BigImage",
            "image_id": "1521359/ffc9c8afbe8b9f6f95c9",
            "title": "ЧТО ТЫ УМЕЕШЬ?",
            "description": """
С помощью навыка можно узнать последние новости из жизни университета, получить информацию о расписании занятий, узнать некоторые важные аспекты учебного процесса.
Для удобства первокурсников в навыке есть специальный раздел, где можно найти полезные советы и информацию о том, как успешно начать свой путь в университете. 
Кроме того, "ИТМО помощник" предоставляет информацию о предметах, которые необходимо изучить в рамках бакалавриата и магистратуры, а также о доступных стипендиях и грантах для студентов.
Для любителей настольных игр в навыке есть возможность сыграть партию шахмат, а для желающих проверить свои знания - интересные викторины и случайные факты об окружающем мире и ИТМО. 
Кроме того, в "ИТМО помощнике" можно найти учебные материалы и методические пособия.
Также для иностранных студентов есть поддержка английского языка.
            """,
        },
    },
    "en-US": {
        "tts": """
        With the help of the skill, you can find out the latest news from the life of the university, get information about the class schedule, learn some important aspects of the educational process.
        For the convenience of first-year students, there is a special section in the skill where you can find useful tips and information on how to successfully start your path at the university.
        In addition, "ITMO Assistant" provides information about the subjects that need to be studied within the bachelor's and master's programs, as well as available scholarships and grants for students.
        For fans of board games, there is an opportunity to play a game of chess in the skill, and for those who want to test their knowledge, there are interesting quizzes and random facts about the world and ITMO.
        In addition, you can find educational materials and teaching aids in ITMO Assistant.
        There is also English language support for foreign students.
        """,
        "buttons": [
            "Repeat",
            "Help",
            "Back",
            "Exit",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1521359/ffc9c8afbe8b9f6f95c9",
            "title": "WHAT CAN YOU DO?",
            "description": """
With the help of the skill, you can find out the latest news from the life of the university, get information about the class schedule, learn some important aspects of the educational process.
For the convenience of first-year students, there is a special section in the skill where you can find useful tips and information on how to successfully start your path at the university.
In addition, "ITMO Assistant" provides information about the subjects that need to be studied within the bachelor's and master's programs, as well as available scholarships and grants for students.
For fans of board games, there is an opportunity to play a game of chess in the skill, and for those who want to test their knowledge, there are interesting quizzes and random facts about the world and ITMO.
In addition, you can find educational materials and teaching aids in ITMO Assistant.
There is also English language support for foreign students.
            """,
        },
    },
}

session_state = {"branch": "whatYouCan"}


def getConfig(event):
    lang = getLanguage(event)
    # lang = "ru-RU"

    return {
        "tts": config[lang]["tts"],
        "buttons": config[lang]["buttons"],
        "card": config[lang]["card"],
        "session_state": session_state,
    }
