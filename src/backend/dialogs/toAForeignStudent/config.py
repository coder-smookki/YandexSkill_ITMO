mainConfig = {
    "ru-RU": {
        "tts": """
    Выберите раздел, который подходит вам:
    Бакалавриат.
    Магистратура.
    Международная Магистратура.
    Дополнительные возможности поступления.
    Миграционные документы.
    """,
        "buttons": [
            "Бакалавриат",
            "Магистратура",
            "Международная Магистратура",
            "Дополнительные возможности поступления",
            "Миграционные документы",
            "Повторить ещё раз",
            "Что ты умеешь?",
            "Помощь",
            "Назад",
            "Выйти",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1030494/e955cc538c12dfb9bd3a",
            "title": "ИНОСТРАННОМУ СТУДЕНТУ",
            "description": """
        Выберите раздел, который подходит вам.
        """,
        },
        "session_state": {"branch": "toAForeignStudent"},
    },
    "en-US": {
        "tts": """
    Choose the section that suits you:
    Undergraduate.
    Master's degree.
    International Master.
    Additional income opportunities.
    Migration documents.
    """,
        "buttons": [
            "Bachelor",
            "Master",
            "International Magistracy",
            "Additional Entry Opportunities",
            "Migration documents" "Say it again",
            "What can you do?",
            "Help",
            "Back",
            "Exit",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1030494/e955cc538c12dfb9bd3a",
            "title": "FOREIGN STUDENT",
            "description": """
        Choose the section that suits you.
        """,
        },
        "session_state": {"branch": "toAForeignStudent"},
    },
}


bechelorConfig = {
    "ru-RU": {
        "tts": """
    Университет ИТМО следует современным тенденциям на рынке труда и в мире научных исследований. 
    Атмосфера неклассического вуза дает возможности для развития полезных навыков и умений у студентов – в образовательной и научной сферах, в предпринимательской, инновационной и социально-ориентированной деятельности. 
    Здесь по-настоящему любят своих студентов, и именно это чувство – любовь – является ключом к пониманию миссии университета, его успехов и достижений.
    Обучение ведется на русском языке. 
    Для иностранных абитуриентов, не владеющих или плохо владеющих русским языком, в Университете ИТМО действует Подготовительное отделение. 
    Программа обучения включает в себя интенсивный курс русского языка и подготовку по профильным предметам, необходимую для сдачи вступительных испытаний.
    Процесс поступления в Университет ИТМО для иностранных граждан практически ничем не отличается от такового для российских абитуриентов – обо всех нюансах вы можете узнать, нажав на кнопку под текстом.
    """,
        "buttons": [
            "Повторить ещё раз",
            "Что ты умеешь?",
            "Помощь",
            "Назад",
            "Выйти",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1030494/e955cc538c12dfb9bd3a",
            "title": "ИНОСТРАННОМУ СТУДЕНТУ (БАКАЛАВРИАТ)",
            "description": """
        Процесс поступления в Университет ИТМО для иностранных граждан практически ничем не отличается от такового для российских абитуриентов – обо всех нюансах вы можете узнать, нажав на кнопку под текстом.
        """,
        },
        "session_state": {"branch": "toAForeignStudent"},
    },
    "en-US": {
        "tts": """
    ITMO University follows modern trends in the labor market and in the world of scientific research.
    The atmosphere of a non-classical university provides opportunities for the development of useful skills and abilities of students - in the educational and scientific fields, in entrepreneurial, innovative and socially-oriented activities.
    Here they really love their students, and it is this feeling - love - that is the key to understanding the mission of the university, its successes and achievements.
    Training is conducted in Russian.
    For foreign applicants who do not speak or have a poor command of Russian, ITMO University has a Preparatory Department.
    The training program includes an intensive Russian language course and training in specialized subjects necessary for passing entrance examinations.
    The process of admission to ITMO University for foreign citizens is practically no different from that for Russian applicants - you can learn about all the nuances by clicking on the button below the text.""",
        "buttons": [
            "Say it again",
            "What can you do?",
            "Help",
            "Back",
            "Exit",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1030494/e955cc538c12dfb9bd3a",
            "title": "FOR A FOREIGN STUDENT (BACHELOR)",
            "description": """
        The process of admission to ITMO University for foreign citizens is practically no different from that for Russian applicants - you can learn about all the nuances by clicking on the button below the text.""",
        },
        "session_state": {"branch": "toAForeignStudent"},
    },
}

magistracyConfig = {
    
}

internationalMagistracyConfig = {
    "tts": """
Хотите вывести своё образование и карьерные перспективы на международный уровень? 
Международные магистерские программы Университета ИТМО – это целый мир новых возможностей и открытий!
Университет ИТМО приглашает бакалавров и специалистов стать частью международных магистерских программ. 
Обучение построено по принципу полного погружения в научную среду и сотрудничества с ведущими международными учеными и экспертами в выбранной области. 
Более того, ряд программ международной магистратуры ИТМО включает в себя уникальную возможность получения двух магистерских дипломов за два года обучения.
    """,
    "buttons": [
        "Повторить ещё раз",
        "Что ты умеешь?",
        "Помощь",
        "Назад",
        "Выйти",
    ],
    "card": {
        "type": "BigImage",
        "image_id": "1030494/e955cc538c12dfb9bd3a",
        "title": "ИНОСТРАННОМУ СТУДЕНТУ (МЕЖДУНАРОДНАЯ МАГИСТРАТУРА)",
        "description": """
        Развивайте карьеру, знакомьтесь с другими культурами и стройте своё будущее!
        """,
    },
    "session_state": {"branch": "toAForeignStudent"},
}

additionalOpportsConfig = {
    "tts": """
    Прием-прием нашим самым классным, умным и талантливым иностранным абитуриентам!
    Как насчет поступить в Университет ИТМО без экзаменов или на бесплатную основу обучения (или, для самых отважных, и то и другое вместе?)
    Мы предлагаем море таких возможностей: для бакалавриата и магистратуры, асов в математике и информатике, гениев русского языка и абитуриентов с уникальными достижениями.
    Выбирай! 
    """,
    "buttons": [
        "Повторить ещё раз",
        "Что ты умеешь?",
        "Помощь",
        "Назад",
        "Выйти",
    ],
    "card": {
        "type": "BigImage",
        "image_id": "1030494/e955cc538c12dfb9bd3a",
        "title": "ДОПОЛНИТЕЛЬНЫЕ ВОЗМОЖНОСТИ ПОСТУПЛЕНИЯ",
        "description": """
        Прием-прием нашим самым классным, умным и талантливым иностранным абитуриентам!
        """,
    },
    "session_state": {"branch": "toAForeignStudent"},
}

migrationDocumentsConfig = {
    "tts": """
ДОКУМЕНТЫ, КОТОРЫЕ НУЖНО ИМЕТЬ ПРИ СЕБЕ, КОГДА ВЫ НАХОДИТЕСЬ НА ТЕРРИТОРИИ РОССИЙСКОЙ ФЕДЕРАЦИИ
Иностранный гражданин (студент) может находиться и свободно перемещаться по территории Российской Федерации лишь при наличии следующих документов:
национальный паспорт (с действующей визой для визовых граждан);
миграционная карта с отметкой о пересечении границы (за исключением граждан Республики Беларусь);
отрывная часть бланка уведомления о прибытии иностранного гражданина/лица без гражданства в РФ по месту вашего временного пребывания (временная регистрация).
    """,
    "buttons": [
        "Повторить ещё раз",
        "Что ты умеешь?",
        "Помощь",
        "Назад",
        "Выйти",
    ],
    "card": {
        "type": "BigImage",
        "image_id": "1030494/e955cc538c12dfb9bd3a",
        "title": "МИГРАЦИОННЫЕ ДОКУМЕНТЫ",
        "description": """
        МИГРАЦИОННАЯ ПОДДЕРЖКА: Адрес - Ул. Ломоносова, д. 9, оф. 2139d, Санкт-Петербург, Россия, 191002. Отдел миграционного учета - ХАЛИЛОВА АЛЕКСАНДРА АХМЕТОВНА. Почта - aakhalilova@itmo.ru. Телефон - +7 (812) 315-05-21
        """,
    },
    "session_state": {"branch": "toAForeignStudent"},
}


def getMainConfig():
    return {
        "tts": mainConfig["tts"],
        "buttons": mainConfig["buttons"],
        "card": mainConfig["card"],
        "session_state": mainConfig["session_state"],
    }


def getBechelorConfig():
    return {
        "tts": bechelorConfig["tts"],
        "buttons": bechelorConfig["buttons"],
        "card": bechelorConfig["card"],
        "session_state": bechelorConfig["session_state"],
    }


def getMagistracyConfig():
    return {
        "tts": magistracyConfig["tts"],
        "buttons": magistracyConfig["buttons"],
        "card": magistracyConfig["card"],
        "session_state": magistracyConfig["session_state"],
    }


def getInternationalMagistracyConfig():
    return {
        "tts": internationalMagistracyConfig["tts"],
        "buttons": internationalMagistracyConfig["buttons"],
        "card": internationalMagistracyConfig["card"],
        "session_state": internationalMagistracyConfig["session_state"],
    }


def getAdditionalOpportsConfig():
    return {
        "tts": additionalOpportsConfig["tts"],
        "buttons": additionalOpportsConfig["buttons"],
        "card": additionalOpportsConfig["card"],
        "session_state": additionalOpportsConfig["session_state"],
    }


def getMigrationDocumentsConfig():
    return {
        "tts": migrationDocumentsConfig["tts"],
        "buttons": migrationDocumentsConfig["buttons"],
        "card": migrationDocumentsConfig["card"],
        "session_state": migrationDocumentsConfig["session_state"],
    }
