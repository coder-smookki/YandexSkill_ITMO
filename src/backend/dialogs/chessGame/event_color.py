from dotenv import load_dotenv; load_dotenv()  # noqa

from dialogs.chessGame import config, event_move


def event_color(event):
    if 'бел' in event["request"]["command"].lower():
        cfg = config.get_config_user_move_first()
        cfg["session_state"]["branch"] = "chessGame"
        cfg["session_state"]["orientation"] = "w"
        return cfg

    if 'черн' in event["request"]["command"].lower():
        event["state"]["session"]["branch"] = "chessGame"
        event["state"]["session"]["orientation"] = 'b'
        return event_move.event_move(event)

    cfg = config.get_config_choose_color()
    cfg["session_state"] = event["state"]["session"]
    return cfg
