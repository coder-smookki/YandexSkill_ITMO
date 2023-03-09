# from main import *
# from student_office import *
from dialogs.allDialogs import allDialogs
# import json
# import requests
# import sqlite3
import time
import json

sessionContexts = {}


def _selectSessionContext(sessionId):
    # connect = sqlite3.connect('sessions.db')
    # cursor = connect.cursor()
    # request = """SELECT * FROM demo LIMIT 1"""
    # cursor.execute(request)
    # ttnw = cursor.fetchone()
    # cursor.close()

    # return ttnw[1]
    if sessionId in sessionContexts:
        return sessionContexts[sessionId]
    return None


def _insertSessionContext(sessionId, context):
    # ts = str(time.time())
    # connect = sqlite3.connect('sessions.db')
    # cursor = connect.cursor()
    # request = f"""
    # INSERT INTO demo (sessionid, context, lastupdate)
    # VALUES ('{sessionId}', '{context}', {ts});
    # """
    # cursor.execute(request)
    # cursor.fetchone()
    # cursor.close()

    # with open('sessionContext.json') as file:
    #     sessionContext = json.loads(file.read())

    sessionContexts[sessionId] = context


def _updateSessionContext(sessionId, context):
    # ts = str(time.time())
    # connect = sqlite3.connect('sessions.db')
    # cursor = connect.cursor()
    # request = f"""
    # UPDATE demo
    # SET context = "{context}", lastupdate = {ts}
    # WHERE sessionid = "{sessionId}";
    # """
    # cursor.execute(request)
    # cursor.fetchone()
    # cursor.close()

    # with open('sessionContext.json') as file:
    #     sessionContext = json.loads(file.read())

    sessionContexts[sessionId] = context


def _getSessionId(event):
    return event['session']['session_id']


def main(event, context):
    # requests.post('https://eotlrqslpj90nwy.m.pipedream.net', json.dumps(sessionContexts))

    for dialog in allDialogs:
        if event['session']['new'] is True:
            _insertSessionContext(_getSessionId(event), dialog['dialogContext'])

        if not dialog['isTriggered'](event, context):
            continue

        event['dialogContext'] = _selectSessionContext(_getSessionId(event))

        if 'dialogContext' in dialog:
            _updateSessionContext(_getSessionId(event), dialog['dialogContext'])

        return dialog['getResponse'](event, context)

    # russian_language_intent = {'русский', 'русски', 'русск', 'русс', 'рус', 'russian', 'russia', 'russi', 'russ', 'rus',
#                            'ru'}

# if event['session']['new'] == True:
#     return general_menu(event, context)
# elif list(set(event['request']['nlu']['tokens']) & {'главное', 'меню'}):
#     return russian_menu(event, context)

# elif 'branch' in event['state']['session']:
#     if list(set(event['request']['nlu']['tokens']) & {'что', 'такое'}) and event['state']['session']['branch'] == 'student_office':
#         return student_office_about(event, context)
# else:
#     requests.post('https://eotlrqslpj90nwy.m.pipedream.net', data='ELSE')
#     if list(set(event['request']['nlu']['tokens']) & russian_language_intent):
#         requests.post('https://eotlrqslpj90nwy.m.pipedream.net', data='RUSSSSSSS')
#         return russian_menu(event, context)
#     if list(set(event['request']['nlu']['tokens']) & {'студенческий', 'офис'}):
#         return student_office_menu(event, context)
#     if list(set(event['request']['nlu']['tokens']) & {'для', 'первокурсников', 'первокурсникам'}):
#         return for_freshmen(event, context)
#     if list(set(event['request']['nlu']['tokens']) & {'расписание', 'занятий'}):
#         return class_timetable_start(event, context)
#     if list(set(event['request']['nlu']['tokens']) & {'расписание', 'сессий'}):
#         return session_timetable(event, context)
#     if list(set(event['request']['nlu']['tokens']) & {'общеуниверситетские', 'модули', 'в', 'бакалавриате'}):
#         return university_wide_modules_in_the_bachelors_degree(event, context)
#     if list(set(event['request']['nlu']['tokens']) & {'общеуниверситетские', 'модули', 'в', 'магистратуре'}):
#         return university_wide_modules_in_the_masters_degree(event, context)
#     if list(set(event['request']['nlu']['tokens']) & {'библиотека'}):
#         return library_category(event, context)
#     if list(set(event['request']['nlu']['tokens']) & {'учебные', 'и', 'методические', 'издания'}):
#         return educational_and_methodological_publications(event, context)
#     if list(set(event['request']['nlu']['tokens']) & {'стипендии'}):
#         return scholarships(event, context)
#     if list(set(event['request']['nlu']['tokens']) & {'задать', 'вопрос'}):
#         return ask_a_question_start(event, context)
#     if list(set(event['request']['nlu']['tokens']) & {'новости'}):
#         return news_category(event, context)


# print(main({
#     "meta": {
#       "locale": "ru-RU",
#       "timezone": "Asia/Yekaterinburg",
#       "client_id": "yabro/23.1.4.778 (none none; Windows 10.0.19044)",
#       "interfaces": {
#           "screen": {},
#           "account_linking": {}
#       }
#       },
#     "session": {
#         "message_id": 0,
#         "session_id": "ded4808c-71ab-41ce-944e-45be4bc3f0bf",
#         "skill_id": "43e4230e-c63a-4a78-9c96-7e5d9f1c0962",
#         "user": {
#             "user_id": "A232D33C64C30FA41BA0857C67B923A01D92955E865EFD8B298D9533FACE16F6"
#         },
#         "application": {
#             "application_id": "903809C39FF095985A4A935C5257FFEE0877A49313E86CADE08D5BBB1D1ABBD4"
#         },
#         "user_id": "903809C39FF095985A4A935C5257FFEE0877A49313E86CADE08D5BBB1D1ABBD4",
#         "new": True
#     },
#     "request": {
#         "command": "",
#         "original_utterance": "",
#         "nlu": {
#             "tokens": [],
#             "entities": [],
#             "intents": {}
#         },
#         "markup": {
#             "dangerous_context": False
#         },
#         "type": "SimpleUtterance"
#     },
#     "state": {
#         "session": {},
#         "user": {},
#         "application": {}
#     },
#     "version": "1.0"
# }, ""))
