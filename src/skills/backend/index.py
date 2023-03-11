from dialogs.allDialogs import allDialogs
from connect import connect
from flask import Flask, request


def main(event, context):
    connect()
    for dialog in allDialogs:
        if not dialog['isTriggered'](event, context):
            continue

        return dialog['getResponse'](event, context)

    

app = Flask(__name__)
@app.route('/', methods=['POST'])
def content():
    data = request.get_json()
    main(data['event'], data['context'])

if __name__ == '__main__':
    app.run()
