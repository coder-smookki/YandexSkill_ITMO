from dialogs.allDialogs import allDialogs
#from connect import connect
from flask import Flask, request
import ssl


def main(event, context):
    for dialog in allDialogs:
        if not dialog['isTriggered'](event, context):
            continue
        return dialog['getResponse'](event, context)


app = Flask(name)
#context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
#context.load_cert_chain('cert.crt')
@app.route('/', methods=['POST'])
def content():
    data = request.get_json()
    print(data)
    reqzap = main(data, None)
    return reqzap


if name == 'main':
#   app.run(port=80, host='0.0.0.0', debug=True, ssl_context=context)
    app.run(port=80, host='0.0.0.0', debug=True)
