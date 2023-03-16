from utils.globalStorage import *
from dialogs.allDialogs import allDialogs
from flask import Flask, request
from middlewares.allMiddlewares import allMiddlewares
from utils.triggerHelper import *
from utils.branchHandler import updateBranchToResponse
import time
from utils.parser.parser import parser
from utils.asyncHelper import doFuncAsAsync
from dotenv import load_env
from utils.responseHelper import *


DIALOG_DEBUG = True
REQUESTS_DEBUG = False

load_env()

def cycleRefreshNews():
    while True:
        print('Start refreshing news')
        setInGlobalStorage('news_announces', parser('announces'), overwrite=True)
        setInGlobalStorage('news_contests', parser('contests'), overwrite=True)
        print('News refreshed')
        time.sleep(3600)


def main(event):
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
        branchedResponse = updateBranchToResponse(event, response, 'russianMenu')
        if DIALOG_DEBUG:
            print('===========================')
        if branchedResponse:
            print('Branch: ' + str(branchedResponse['session_state']['branch']))
        else:
            print("Branch don't initilized")
        print('---------------------------')
        print(getState(event, 'timeTable_group'))
        print(getState(event, 'timeTable_course'))
        return branchedResponse


app = Flask(__name__)
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

    app.run()
    print('Shutdown!')
