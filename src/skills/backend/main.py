from flask import Flask, request
import json

app = Flask(__name__)

sessionStorage = {}


# Главная функция которая запускает обработчик диалогового окна
@app.route('/post', methods=['POST'])
def main():
    response = \
        {
            'session': request.json['session'],
            'version': request.json['version'],
            'response': {
                'end_session': False
            }
        }
    handle_dialog(request.json, response)
    return json.dumps(response, ensure_ascii=False)


# Функция обработки диалогового окна
def handle_dialog(req, res):
    user_id = req['session']['user_id']
    if req['session']['new']:
        sessionStorage[user_id] = \
            {
                'suggests': [
                    'Русский Язык',
                    'Английский язык',
                    'Выйти',
                    'Помощь'
                ]
            }
        res['response']['text'] = \
            """
Привет Студент! Чтобы пользоваться навыком, выбери язык.

Hello Student! To use the skill, choose a language.

        1. Русский Язык (Russian Language)
        2. Английский Язык (English Language)
            """
        res['response']['buttons'] = [
            {
                'title': button,
                'hide': True
            } for button in sessionStorage[user_id]['suggests']
        ]
        res['response']['card'] = {
            "type": "BigImage",
            "image_id": '',
            "title": '',
            "description": ''
        }
        return
    else:
        tokens = req['request']['nlu']['tokens']
        russian_language_intent = {'Русский Язык', 'Русский', 'Русс', 'Рус', 'Ру', 'Русск', 'Рсскй', 'Рсский', 'Русскй',
                                   'Russian Language', 'Russian', 'Russ', 'Rus', 'Ru', 'Russin', 'Rssn', 'Russn',
                                   'русский язык', 'Русский язык', 'русский Язык' 'русский', 'русс', 'рус', 'ру',
                                   'русск', 'рсскй', 'рсский', 'русскй', 'Russian language', 'russian Language',
                                   'russian', 'russ', 'rus', 'ru', 'russin', 'rssn', 'russn'}
        english_language_intent = {'English language', 'english language', 'English Language', 'english Language',
                                   'Английский Язык', 'английский язык', 'Английский язык', 'английский Язык',
                                   'Английский', 'английский', 'англ', 'Англ', 'Англский', 'англский', 'Англск',
                                   'англск', 'English', 'english', 'En', 'Englsh', 'Engish', 'en', 'englsh', 'engish',
                                   'Eng', 'eng', }
        exit_skills_intent = {'Выйти', 'выйти', 'вйти', 'Вйти', 'выходи', 'exit', 'Exit', 'Ext', 'ext', 'выход'}
        help_skills_intent = {'Помощь', 'помощь', 'пмщь', 'Пмщь', 'Help', 'help'}
        if list(set(tokens) & russian_language_intent):
            pass
        if list(set(tokens) & english_language_intent):
            pass
        if list(set(tokens) & exit_skills_intent):
            pass
        if list(set(tokens) & help_skills_intent):
            pass


# Запуск программы
if __name__ == '__main__':
    app.run()
