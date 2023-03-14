from dialogs.allDialogs import allDialogs
from flask import Flask, request
from middlewares.allMiddlewares import allMiddlewares
from utils.triggerHelper import *
from utils.branchHandler import updateBranchToResponse

DEBUG = True

def main(event, context):
    if DEBUG:
        if 'branch' in event['state']['session']:
            print('Branch: ' + event['state']['session']['branch'])
        else:
            print("Branch don't initilized")
        print('---------------------------')
    if not isNewSession(event):
        for key in allMiddlewares:
            if not allMiddlewares[key]['isTriggered'](event, context):
                continue
            return allMiddlewares[key]['getResponse'](event, allDialogs)

    for key in allDialogs:
        if DEBUG:
            print(str(key) + ' ' + str(allDialogs[key]['isTriggered'](event, context)))
            print('===========================')
        if not allDialogs[key]['isTriggered'](event, context):
            continue
        response = allDialogs[key]['getResponse'](event, context)
        branchedResponse = updateBranchToResponse(event, response)
        return branchedResponse

app = Flask(__name__)

@app.route('/', methods=['POST'])
def content():
    data = request.get_json()
    # print(f"""                                                                                                                                                     |
    # ЗАПРОС КОТОРЫЙ ПОСТУПИЛ НАМ!                                                                                                                                       |
    # {data}                                                                                                                                                             |
    # """) 
    reqzap = main(data, None)
    # print(f"""                                                                                                                                                     |
    # ЗАПРОС КОТОРЫЙ ОТПРАВИЛИ МЫ!                                                                                                                                            |
    # {reqzap}                                                                                                                                                           |
    # """)
    return reqzap


if __name__ == '__main__':
    print('Server starting...')

    app.run(port=2083, host='0.0.0.0', debug=True)
    print('Shutdown!')
