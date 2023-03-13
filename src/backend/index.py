from dialogs.allDialogs import allDialogs
from flask import Flask, request
from middlewares.allMiddlewares import allMiddlewares

def main(event, context):
    for key in allMiddlewares:
        if not allMiddlewares[key]['isTriggered'](event, allDialogs):
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
    print(data)
    reqzap = main(data, None)
    return reqzap


if __name__ == 'main':
    app.run(port=2083, host='0.0.0.0', debug=True)
