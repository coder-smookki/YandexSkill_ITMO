from dotenv import load_dotenv; load_dotenv()  # noqa

from dialogs.chessGame import config, event_move


def event_color(event):
    if 'бел' in event["request"]["command"].lower():
        return config.get_config_user_move_first()

    if 'черн' in event["request"]["command"].lower().replace('ё', 'e'):
        # event["state"]["session"]["branch"] = "chessGame"
        # event["state"]["session"]["orientation"] = 'b'
        return config.get_config_user_move_second()
        # return event_move.event_move(event)

    cfg = config.get_config_choose_color()
    return cfg
