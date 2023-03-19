from dotenv import load_dotenv;

load_dotenv()  # noqa

from dialogs.chessGame import config, event_move


def event_color(event):
    if 'белы' in event["request"]["command"].lower():
        return config.get_config_user_move_first()

    if 'черн' in event["request"]["command"].lower() or 'чёрн' in event["request"]["command"].lower():
        return config.get_config_user_move_second()

    return config.get_config_choose_color()
