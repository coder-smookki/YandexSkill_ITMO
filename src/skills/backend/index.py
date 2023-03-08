from dialogs.allDialogs import allDialogs


def main(event, context):
    # requests.post('https://eotlrqslpj90nwy.m.pipedream.net', data="main")
    for dialog in allDialogs:
        if not dialog['isTriggered'](event, context):
            continue
        return dialog['getResponse'](event, context)