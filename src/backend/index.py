from dialogs.allDialogs import allDialogs
from flask import Flask, request
from middlewares.allMiddlewares import allMiddlewares
from utils.triggerHelper import *


def main(event, context):
    if not isNewSession(event):
        for key in allMiddlewares:
            if not allMiddlewares[key]['isTriggered'](event, context):
                continue
            return allMiddlewares[key]['getResponse'](event, allDialogs)
    for key in allDialogs:
        if not allDialogs[key]['isTriggered'](event, context):
            continue
        return allDialogs[key]['getResponse'](event, context)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def content():
    data = request.get_json()
    print(f"""                                                                                                                                                     |
    ЗАПРОС КОТОРЫЙ ПОСТУПИЛ НАМ!                                                                                                                                       |
    {data}                                                                                                                                                             |
    """) 
    reqzap = main(data, None)
    print(f"""                                                                                                                                                     |
    ЗАПРОС КОТОРЫЙ ОТПРАВИЛИ МЫ!                                                                                                                                            |
    {reqzap}                                                                                                                                                           |
    """)
    return reqzap


if __name__ == '__main__':
    print('Server starting...')
    app.run(port=2083, host='0.0.0.0', debug=True)
    print('Shutdown!')
