from flask import Flask, request
import json

app = Flask(__name__)

sessionStorage = {}


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
    general_menu(request.json, response)
    return json.dumps(response, ensure_ascii=False)


def general_menu(req, res):
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
        res['response']['buttons'] = sessionStorage[user_id]
        return


if __name__ == '__main__':
    app.run()
