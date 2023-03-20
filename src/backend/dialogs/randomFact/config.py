import random
from utils.responseHelper import getGlobalState, getLanguage

config = {
    "ru-RU": {
        'facts': [
    "Опросы показывают, что студенты, которые принимают заметки вручную, имеют более высокие оценки, чем те, кто использует ноутбуки для заметок. Один из возможных объяснений этого явления заключается в том, что ручное письмо способствует более глубокому пониманию материала.",
    "Исследования показывают, что физическая активность, такая как занятия спортом, может помочь студентам улучшить свои результаты в учебе. Это связано с тем, что упражнения способствуют лучшему кровообращению в мозге и улучшению когнитивных функций.",
    "Учёные утверждают, что обучение в группах может способствовать более эффективному усвоению материала. Общение со своими коллегами может помочь студентам более глубоко понять тему и осознать её применение в реальной жизни.",
    "Сон играет важную роль в учебном процессе. Исследования показывают, что студенты, которые получают достаточно сна, имеют лучшие результаты в учебе, чем те, кто страдает от недостатка сна. Для взрослых людей рекомендуется спать от 7 до 9 часов в сутки.",
    "Учёные также говорят, что регулярные перерывы во время учебы могут помочь улучшить ваши результаты. Это связано с тем, что наш мозг может лучше обрабатывать информацию, когда мы регулярно меняем вид деятельности.",
    "Исследования показывают, что использование цвета при заметках и выделении ключевых слов в тексте может помочь улучшить запоминание информации. Это может быть особенно полезно при подготовке к экзаменам.",
    "Студенты, которые занимаются спортом, обычно имеют лучшие результаты в учёбе, чем те, кто не занимается спортом.",
    "Некоторые исследования показывают, что люди лучше запоминают информацию, когда они её записывают вручную, а не печатают на компьютере.",
    "Чтение вслух может помочь студентам запомнить информацию лучше, чем просто чтение в уме.",
    "Студенты, которые спят достаточно, часто имеют лучшие результаты в учёбе, чем те, кто не высыпается.",
    "Исследования показывают, что студенты, которые занимаются в комнате с ярким освещением, имеют лучшие результаты в учёбе, чем те, кто занимается в темном помещении.",
    "Некоторые эксперты советуют заниматься физическими упражнениями перед началом учёбы, чтобы улучшить кровообращение в мозге и улучшить способность к концентрации.",
    "Студенты, которые пользуются цветными ручками при записи лекций и заметок, лучше запоминают информацию, чем те, кто использует только один цвет.",
    "Регулярное повторение и закрепление материала, которое происходит в течение длительного периода времени, помогает улучшить запоминание и уменьшить забывание.",
    "Использование мнемоников, таких как акронимы, помогает запоминать и организовывать информацию.",
    "Изучение предмета на практике может помочь лучше понять теоретический материал. Например, при изучении языка, можно попрактиковаться в общении на этом языке с носителями.",
    "Некоторые исследования показывают, что небольшие паузы во время учёбы, когда вы занимаетесь чем-то другим, могут помочь улучшить запоминание информации.",
    "Постоянное участие в академических мероприятиях, таких как лекции, семинары и конференции, может помочь улучшить понимание и знания в вашей области.",
    "Чтение и написание своих собственных заметок может помочь вам улучшить понимание материала и организовать свои мысли.",
    "Сон играет важную роль в процессе запоминания и консолидации информации. Старайтесь спать достаточное количество часов, чтобы ваш мозг мог обработать и закрепить информацию, полученную в течение дня."
        ],
        "message": 'Случайный факт: \n',
        "buttons": [
            "Еще факт",
            "Повторить ещё раз",
            'Что ты умеешь?',
            "Помощь",
            "Назад",
            "Выйти"
        ],
    },

    "en-US": {
        'facts': [
    "Surveys show that students who take notes by hand score higher than those who use laptops to take notes. One possible explanation for this phenomenon is that handwriting contributes to a deeper understanding of the material.",
    "Studies show that physical activity, such as playing sports, can help students improve their academic performance. This is because exercise improves blood flow to the brain and improves cognitive function.",
    "Scientists argue that learning in groups can contribute to more effective assimilation of the material. Communication with their colleagues can help students understand the topic more deeply and realize its application in real life.",
    "Sleep plays an important role in the learning process. Research shows that students who get enough sleep have better academic results than those who suffer from lack of sleep. For adults, it is recommended to sleep 7 to 9 hours a night.",
    "Scientists also say that taking regular breaks while studying can help improve your performance. This is because our brains can process information better when we change activities regularly.",
    "Studies show that using color when taking notes and highlighting key words in text can help improve information retention. This can be especially helpful when preparing for exams.",
    "Students who play sports usually have better academic results than those who do not play sports.",
    "Some research shows that people remember information better when they write it down by hand, rather than typing it on a computer.",
    "Reading aloud can help students remember information better than just reading in their heads.",
    "Students who get enough sleep often have better academic results than those who don't.",
    "Studies show that students who study in a brightly lit room have better academic results than those who study in a dark room.",
    "Some experts advise exercising before studying to improve blood circulation in the brain and improve the ability to concentrate.",
    "Students who use colored pens to write lectures and notes retain information better than those who use only one color.",
    "Regular repetition and reinforcement over a long period of time helps improve retention and reduce forgetting.",
    "Using mnemonics such as acronyms helps memorize and organize information.",
    "Studying the subject in practice can help you better understand the theoretical material. For example, when learning a language, you can practice communicating in this language with native speakers.",
    "Some research shows that taking small breaks while you're studying while you're doing something else can help improve memory retention.",
    "Continued participation in academic activities such as lectures, seminars, and conferences can help improve understanding and knowledge in your field.",
    "Reading and writing your own notes can help you improve your understanding and organize your thoughts.",
    "Sleep plays an important role in the process of remembering and consolidating information. Try to get enough sleep so that your brain can process and consolidate the information received during the day."
        ],
        "message": 'Random fact: \n',
        "buttons": [
            "Another fact",
            "Repeat",
            "What can you do?",
            "Help",
            "Back",
            "Exit",

        ],
    }
}

session_state = {
    "branch": "randomFact"
}


def getConfig(event):
    lang = getLanguage(event)
    # lang = "ru-RU"
    messageResponse = config[lang]["message"] + config[lang]['facts'][random.randint(0, len(config[lang]['facts']))]

    return {
        "message": messageResponse,
        "tts": messageResponse,
        "buttons": config[lang]["buttons"],
        "session_state": session_state,
    }

