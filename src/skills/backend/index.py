from main import *
from student_office import *
import requests
import json

russian_language_intent = {'русский', 'русски', 'русск', 'русс', 'рус', 'russian', 'russia', 'russi', 'russ', 'rus',
                           'ru'}


def main(event, context):
    jsonchik = json.dumps(event)
    body = {"result_main": jsonchik}
    r = requests.post('https://eotlrqslpj90nwy.m.pipedream.net/', data=body)
    if event['session']['new'] == True:
        return general_menu(event, context)
    elif list(set(event['request']['nlu']['tokens']) & {'главное', 'меню'}):
        return russian_menu(event, context)
    elif 'branch' in event['state']['session']:
        if list(set(event['request']['nlu']['tokens']) & {'что', 'такое'}) and event['state']['session'][
            'branch'] == 'student_office':
            return student_office_about(event, context)
    else:
        if list(set(event['request']['nlu']['tokens']) & russian_language_intent):
            return russian_menu(event, context)
        if list(set(event['request']['nlu']['tokens']) & {'студенческий', 'офис'}):
            return student_office_menu(event, context)
        if list(set(event['request']['nlu']['tokens']) & {'для', 'первокурсников', 'первокурсникам'}):
            return for_freshmen(event, context)
        if list(set(event['request']['nlu']['tokens']) & {'расписание', 'занятий'}):
            return class_timetable_start(event, context)
        if list(set(event['request']['nlu']['tokens']) & {'расписание', 'сессий'}):
            return session_timetable(event, context)
        if list(set(event['request']['nlu']['tokens']) & {'общеуниверситетские', 'модули', 'в', 'бакалавриате'}):
            return university_wide_modules_in_the_bachelors_degree(event, context)
        if list(set(event['request']['nlu']['tokens']) & {'общеуниверситетские', 'модули', 'в', 'магистратуре'}):
            return university_wide_modules_in_the_masters_degree(event, context)
        if list(set(event['request']['nlu']['tokens']) & {'библиотека'}):
            return library_category(event, context)
        if list(set(event['request']['nlu']['tokens']) & {'учебные', 'и', 'методические', 'издания'}):
            return educational_and_methodological_publications(event, context)
        if list(set(event['request']['nlu']['tokens']) & {'стипендии'}):
            return scholarships(event, context)
        if list(set(event['request']['nlu']['tokens']) & {'задать', 'вопрос'}):
            return ask_a_question_start(event, context)
        if list(set(event['request']['nlu']['tokens']) & {'новости'}):
            return news_category(event, context)