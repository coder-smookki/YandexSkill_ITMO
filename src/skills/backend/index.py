from dialogs.allDialogs import allDialogs
from connect import connect


def main(event, context):
    connect()
    for dialog in allDialogs:
        if not dialog['isTriggered'](event, context):
            continue

        return dialog['getResponse'](event, context)
