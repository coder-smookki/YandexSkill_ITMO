from dialogs.allDialogs import allDialogs
from flask import Flask, request
from middlewares.allMiddlewares import allMiddlewares
from utils.triggerHelper import *
from utils.branchHandler import updateBranchToResponse
import random

DIALOG_DEBUG = True
REQUESTS_DEBUG = True

def main(event):
    if DIALOG_DEBUG:
        print('===========================')
        if 'branch' in event['state']['session']:
            print('Branch: ' + str(event['state']['session']['branch']))
        else:
            print("Branch don't initilized")
        print('---------------------------')
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
        return branchedResponse
    if DIALOG_DEBUG:
        print('===========================')

app = Flask(__name__)

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

    app.run(port=2083, host='0.0.0.0', debug=True)
    print('Shutdown!')
