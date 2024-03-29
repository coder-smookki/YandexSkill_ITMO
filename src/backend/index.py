import os
from utils.globalStorage import *
from dialogs.allDialogs import allDialogs
from flask import Flask, request
from middlewares.allMiddlewares import allMiddlewares
from utils.triggerHelper import *
from utils.branchHandler import updateBranchToResponse
import time
from utils.parser.parser import parser
from utils.asyncHelper import doFuncAsAsync
from utils.responseHelper import *
from dotenv import load_dotenv

DIALOG_DEBUG = False
REQUESTS_DEBUG = False

load_dotenv()


def cycleRefreshNews():
    while True:
        print('Start refreshing news')
        setInGlobalStorage('news_announces_ru-RU', parser('announces', '', 'ru-RU'), overwrite=True)
        setInGlobalStorage('news_contests_ru-RU', parser('contests', '', 'ru-RU'), overwrite=True)
        setInGlobalStorage('news_announces_en-US', parser('announces', '', 'en-US'), overwrite=True)
        setInGlobalStorage('news_contests_en-US', parser('contests', '', 'en-US'), overwrite=True)
        print('News refreshed')
        time.sleep(3600)


def main(event):
    if 'session' in event and 'skill_id' in event['session'] and event['session']['skill_id'] != os.environ['SKILL_ID']:
        return 'привет =)'
    if DIALOG_DEBUG:
        print('===========================')
    if not isNewSession(event):
        for key in allMiddlewares:
            if not allMiddlewares[key]['isTriggered'](event):
                continue
            return allMiddlewares[key]['getResponse'](event, allDialogs)

    for key in allDialogs:
        if DIALOG_DEBUG:
            print(str(key) + ' ' + str(allDialogs[key]['isTriggered'](event)))
        if not allDialogs[key]['isTriggered'](event):
            continue
        response = allDialogs[key]['getResponse'](event, allDialogs)
        branchedResponse = updateBranchToResponse(event, response, 'mainMenu')
        if DIALOG_DEBUG:
            print('===========================')
        if branchedResponse and 'session_state' in branchedResponse:
            print('Branch: ' + str(branchedResponse['session_state']['branch']))
        else:
            print("Branch don't initilized")
        print('---------------------------')

        return branchedResponse


app = Flask(__name__)

app.config['SKILL_ID'] = os.environ['SKILL_ID']

setInGlobalStorage('app', app, saveLinks=True)
doFuncAsAsync(cycleRefreshNews)


@app.route('/', methods=['POST'])
def content():
    data = request.get_json()
    if REQUESTS_DEBUG:
        print(f"""                                                                                                                                                     |
        ЗАПРОС КОТОРЫЙ ПОСТУПИЛ НАМ!                                                                                                                                       |
        {data}                                                                                                                                                             |
        """)
    reqzap = main(data)
    if REQUESTS_DEBUG:
        print(f"""                                                                                                                                                     |
        ЗАПРОС КОТОРЫЙ ОТПРАВИЛИ МЫ!                                                                                                                                            |
        {reqzap}                                                                                                                                                           |
        """)
    return reqzap


if __name__ == '__main__':
    print('Server starting...')

    app.run(host='0.0.0.0', port=2083)
    print('Shutdown!')
