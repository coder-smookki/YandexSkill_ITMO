from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        "message":
            """
Вот полные подробности о нашем навыке:

Новости - Просматривайте такие категории новостей, как "анонсы" и "контесты".
Студенческий офис - Ответы на часто задаваемые вопросы студентов.
Первокурсникам - Полезная информация для первокурсников.
Расписание занятий - Просмотр расписаний для вашей группы.
Общеуниверситетские модули - то, с чего начинается обучение в Университете ИТМО как в бакалавриате, так и в магистратуре.
Иностранному студенту - Ответы на часто задаваемые вопросы иностранных студентов.
Библиотека - это центр, предоставляющий все возможности для вашего профессионального роста и развития:
Учебные и методические издания - Найдите издания, представляющие интерес.
Стипендии - Информация о стипендиях и её категориях.
Шахматы - Замечательная игра, в которой студент сможет отвлечься.
Викторина - Вопросы по математике, информационным технологиям и другим областям.
Случайный факт - Узнайте что-то новое.
            """,
        "tts":
            """
Вот полные подробности о нашем навыке:

Новости, Просматривайте такие категории новостей, как "анонсы" и "контесты".
Студенческий офис, Ответы на часто задаваемые вопросы студентов.
Первокурсникам, Полезная информация для первокурсников.
Расписание занятий, Просмотр расписаний для вашей группы.
Общеуниверситетские модули, то, с чего начинается обучение в Университете ИТМО как в бакалавриате, так и в магистратуре.
Иностранному студенту, Ответы на часто задаваемые вопросы иностранных студентов.
Библиотека, это центр, предоставляющий все возможности для вашего профессионального роста и развития:
Учебные и методические издания, Найдите издания, представляющие интерес.
Стипендии, Информация о стипендиях и её категориях.
Шахматы, Замечательная игра, в которой студент сможет отвлечься.
Викторина, Вопросы по математике, информационным технологиям и другим областям.
Случайный факт, Узнайте что-то новое.
            """,
        "buttons": ["Повторить ещё раз", "Что ты умеешь?", "Назад", "Выйти"],
    },
    "en-US": {
        "message":
            """
Here are the full details about our skill:

News - View news categories such as "announcements" and "contests".
Student Office - Answers to frequently asked questions of students.
Freshmen - Useful information for freshmen.
Class Schedule - View schedules for your group.
University-wide modules are the starting point for studying at ITMO University in both bachelor's and master's degrees.
For a foreign student - Answers to frequently asked questions of foreign students.
The library is a center that provides all the opportunities for your professional growth and development:
Educational and methodological publications - Find publications of interest.
Scholarships - Information about scholarships and its categories.
Chess is a wonderful game in which a student can get distracted.
Quiz - Questions on mathematics, information technology and other fields.
Random fact - Learn something new.
            """,
        "tts":
            """
Here are the full details about our skill:

News, View news categories such as "announcements" and "contests".
Student office, Answers to frequently asked questions of students.
Freshmen, Useful information for freshmen.
Class schedule, View schedules for your group.
University-wide modules, the beginning of education at ITMO University in both bachelor's and master's degrees.
For a foreign student, Answers to frequently asked questions of foreign students.
The library is a center that provides all the opportunities for your professional growth and development:
Educational and methodological publications, Find publications of interest.
Scholarships, Information about scholarships and its categories.
Chess is a wonderful game in which a student can distract himself.
Quiz, Questions on mathematics, information technology and other fields.
Random fact, Learn something new.
            """,
        "buttons": [
            "Repeat",
            "What can you do?",
            "Back",
            "Exit",
        ],
    },
}

session_state = {"branch": "learnMoreAboutTheSkill"}


def getConfig(event):
    lang = getLanguage(event)
    # lang = "ru-RU"

    return {
        "message": config[lang]["message"],
        "tts": config[lang]["tts"],
        "buttons": config[lang]["buttons"],
        "session_state": session_state,
    }
