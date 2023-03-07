from main import general_menu
from main import russian_menu
from main import student_office_menu
from student_office import student_office_about

russian_language_intent = {'русский', 'русски', 'русск', 'русс', 'рус', 'russian', 'russia', 'russi', 'russ', 'rus',
                           'ru'}


def main(event, context):
    if event['session']['new'] == True:
        return general_menu(event, context)
    elif event['command'] == 'главное меню':
        return russian_menu(event, context)
    elif 'branch' in event['state']['session']:
        if list(set(event['request']['nlu']['tokens']) & {'что', 'такое'}) and event['state']['session']['branch'] == 'student_office':
            return student_office_about(event, context)
    else:
        if list(set(event['request']['nlu']['tokens']) & russian_language_intent):
            return russian_menu(event, context)
        if list(set(event['request']['nlu']['tokens']) & {'студенческий', 'офис'} or event['request']['command'] == "студенческий офис"):
            return student_office_menu(event, context)