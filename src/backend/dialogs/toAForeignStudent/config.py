from utils.responseHelper import getLanguage

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
            "Migration Documents",
            "Repeat",
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
        The process of admission to ITMO University for foreign citizens is practically no different from that for Russian applicants - you can learn about all the nuances by clicking on the button below the text.
        """,
        "buttons": [
            "Repeat",
            "What can you do?",
            "Help",
            "Back",
            "Exit",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1030494/e955cc538c12dfb9bd3a",
            "title": "FOR A FOREIGN STUDENT (BACHELOR STUDENT)",
            "description": """
            The process of admission to ITMO University for foreign citizens is practically no different from that for Russian applicants - you can learn about all the nuances by clicking on the button below the text.
            """,
        },
        "session_state": {"branch": "toAForeignStudent"},
    },
}

magistracyConfig = {
    "ru-RU": {
        "tts": """
        Университет ИТМО – ведущий вуз России в области информационных и фотонных технологий, а также один из немногих российских вузов, имеющих статус национального исследовательского университета. 
        ИТМО уже более 15 лет успешно проводит программы подготовки магистров.
        Ежегодно Университет ИТМО набирает студентов на более чем сотню магистерских программ по многочисленным направлениям подготовки в области информационных и оптических технологий, экономики, защиты окружающей среды, метрологии, телекоммуникаций, фотоники, технической физики. 
        К моменту завершения обучения значительная часть выпускников имеет внушительное портфолио для поступления в аспирантуру.
        Обучение в магистратуре ведется по очной и заочной форме. Набор производится на бюджетной и платной основе. Продолжительность обучения – 2 года.
        Для иностранных абитуриентов, не владеющих или плохо владеющих русским языком, в Университете ИТМО действует Подготовительное отделение.
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
            "title": "ИНОСТРАННОМУ СТУДЕНТУ (МАГИСТРАТУРА)",
            "description": """
            Процесс поступления в Университет ИТМО для иностранных граждан практически ничем не отличается от такового для российских абитуриентов – обо всех нюансах вы можете узнать, нажав на кнопку под текстом.
            """,
        },
        "session_state": {"branch": "toAForeignStudent"},
    },
    "en-US": {
        "tts": """
        ITMO University is a leading Russian university in the field of information and photonic technologies, and one of the few Russian universities with the status of a national research university.
        For more than 15 years, ITMO has been successfully running master's degree programs.
        Every year, ITMO University recruits students for more than a hundred master's programs in numerous fields of study in information and optical technologies, economics, environmental protection, metrology, telecommunications, photonics, and technical physics.
        By the time they complete their studies, a significant part of graduates have an impressive portfolio for admission to graduate school.
        Education in the magistracy is conducted on a full-time and part-time basis. The set is made on a budgetary and paid basis. The duration of training is 2 years.
        For foreign applicants who do not speak or have a poor command of Russian, ITMO University has a Preparatory Department.
        """,
        "buttons": [
            "Repeat",
            "What can you do?",
            "Help",
            "Back",
            "Exit",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1030494/e955cc538c12dfb9bd3a",
            "title": "FOR A FOREIGN STUDENT (MASTER)",
            "description": """
            The process of admission to ITMO University for foreign citizens is practically no different from that for Russian applicants - you can learn about all the nuances by clicking on the button below the text.
            """,
        },
        "session_state": {"branch": "toAForeignStudent"},
    },
}

internationalMagistracyConfig = {
    "ru-RU": {
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
    },
    "en-US": {
        "tts": """
        Do you want to take your education and career prospects to the international level?
        International master's programs at ITMO University are a whole world of new opportunities and discoveries!
        ITMO University invites bachelors and specialists to become part of international master's programs.
        The training is built on the principle of full immersion in the scientific environment and cooperation with leading international scientists and experts in the chosen field.
        Moreover, a number of ITMO's international master's programs include a unique opportunity to receive two master's degrees in two years of study.
        """,
        "buttons": [
            "Repeat",
            "What can you do?",
            "Help",
            "Back",
            "Exit",
        ],
        "card": {
            "type": "BigImage",
            "image_id": "1030494/e955cc538c12dfb9bd3a",
            "title": "FOR A FOREIGN STUDENT (INTERNATIONAL MASTER)",
            "description": """Develop your career, meet other cultures and build your future!""",
        },
        "session_state": {"branch": "toAForeignStudent"},
    },
}

additionalOpportsConfig = {
    "ru-RU": {
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
    },
    "en-US": {
        "tts": """
    Welcome to our coolest, smartest and most talented international students!
     How about entering ITMO University without exams or on a free basis of study (or, for the most courageous, both?)
     We offer a sea of such opportunities: for undergraduate and graduate students, aces in mathematics and computer science, geniuses of the Russian language and applicants with unique achievements.
     Choose! 
    """,
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
            "title": "ADDITIONAL ENTRY OPPORTUNITIES",
            "description": """Welcome to our coolest, smartest and most talented international students!""",
        },
        "session_state": {"branch": "toAForeignStudent"},
    },
}

migrationDocumentsConfig = {
    "ru-RU": {
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
    },
    "en-US": {
        "tts": """
DOCUMENTS YOU SHOULD HAVE WITH YOU WHEN YOU ARE IN THE RUSSIAN FEDERATION
A foreign citizen (student) may stay and move freely within the territory of the Russian Federation only if he/she has the following documents:
national passport (with a valid visa for visa citizens);
migration card with a mark on crossing the border (except for citizens of the Republic of Belarus);
a detachable part of the form of notification of the arrival of a foreign citizen/stateless person in the Russian Federation at the place of your temporary stay (temporary registration).    """,
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
            "title": "MIGRATION DOCUMENTS",
            "description": """
        MIGRATION SUPPORT: Address - st. Lomonosov, d. 9, of. 2139d, St. Petersburg, Russia, 191002. Department of Migration Registration - KHALILOVA ALEKSANDRA AKHMETOVNA. Mail - aakhalilova@itmo.ru. Phone - +7 (812) 315-05-21""",
        },
        "session_state": {"branch": "toAForeignStudent"},
    },
}


def getMainConfig(event):
    lang = getLanguage(event)
    return {
        "tts": mainConfig[lang]["tts"],
        "buttons": mainConfig[lang]["buttons"],
        "card": mainConfig[lang]["card"],
        "session_state": mainConfig[lang]["session_state"],
    }


def getBechelorConfig(event):
    lang = getLanguage(event)
    return {
        "tts": bechelorConfig[lang]["tts"],
        "buttons": bechelorConfig[lang]["buttons"],
        "card": bechelorConfig[lang]["card"],
        "session_state": bechelorConfig[lang]["session_state"],
    }


def getMagistracyConfig(event):
    lang = getLanguage(event)
    return {
        "tts": magistracyConfig[lang]["tts"],
        "buttons": magistracyConfig[lang]["buttons"],
        "card": magistracyConfig[lang]["card"],
        "session_state": magistracyConfig[lang]["session_state"],
    }


def getInternationalMagistracyConfig(event):
    lang = getLanguage(event)
    return {
        "tts": internationalMagistracyConfig[lang]["tts"],
        "buttons": internationalMagistracyConfig[lang]["buttons"],
        "card": internationalMagistracyConfig[lang]["card"],
        "session_state": internationalMagistracyConfig[lang]["session_state"],
    }


def getAdditionalOpportsConfig(event):
    lang = getLanguage(event)
    return {
        "tts": additionalOpportsConfig[lang]["tts"],
        "buttons": additionalOpportsConfig[lang]["buttons"],
        "card": additionalOpportsConfig[lang]["card"],
        "session_state": additionalOpportsConfig[lang]["session_state"],
    }


def getMigrationDocumentsConfig(event):
    lang = getLanguage(event)
    return {
        "tts": migrationDocumentsConfig[lang]["tts"],
        "buttons": migrationDocumentsConfig[lang]["buttons"],
        "card": migrationDocumentsConfig[lang]["card"],
        "session_state": migrationDocumentsConfig[lang]["session_state"],
    }
