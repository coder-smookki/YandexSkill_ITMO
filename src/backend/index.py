from dialogs.allDialogs import allDialogs
from flask import Flask, request
from middlewares.allMiddlewares import allMiddlewares
from utils.triggerHelper import *


def updateBranch(event, response):
    if not 'branch' in event['state']['session']:
        response['response']['session_state']['branch'] = []
        return response
    else:
        eventbranch = event['state']['session']['branch']
        responseState = response['response']['session_state']

        # сработает, если eventbranch.index(...) найдет новый брэнч в брэнчах
        try:
            index = eventbranch.index(responseState)
            eventbranch = eventbranch[0:index]
            eventbranch.append(responseState)
            response['response']['session_state']['branch'] = eventbranch
            return response
        # в случае, если в брэнчах нету нового бренча
        except:
            eventbranch.append(responseState)
            response['response']['session_state']['branch'] = eventbranch
            return response



def main(event, context):
    if not isNewSession(event):
        for key in allMiddlewares:
            if not allMiddlewares[key]['isTriggered'](event, context):
                continue
            return allMiddlewares[key]['getResponse'](event, allDialogs)
    for key in allDialogs:
        if not allDialogs[key]['isTriggered'](event, context):
            continue
        response = allDialogs[key]['getResponse'](event, context)
        branchedResponse = updateBranch(event, response)
        return branchedResponse

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
