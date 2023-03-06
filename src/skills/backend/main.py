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
    handle_dialog(request.json, response)
    return json.dumps(response)


def handle_dialog(req, res):
    user_id = req['session']['user_id']
    if req['session']['new']:
        sessionStorage[user_id] = \
            {
                'suggests': [
                    None
                ]
            }
        res['response']['text'] = \
            """
Привет Студент! Чтобы пользоваться навыком, выбери язык.

Hello Student! To use the skill, choose a language.


        1. Русский Язык (Russian Language)
        2. Английский Язык (English Language)
            """

        return sessionStorage


if __name__ == '__main__':
    app.run()
