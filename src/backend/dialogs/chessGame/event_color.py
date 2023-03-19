from dotenv import load_dotenv
load_dotenv()

from utils.responseHelper import *

from dialogs.chessGame import config, event_move


def event_color(event):
    lang = getLanguage(event)
    if 'белы' in event["request"]["command"].lower() or 'white' in event["request"]["command"].lower():
        return config.get_config_user_move_first(lang)

    if ('черн' in event["request"]["command"].lower() or 'чёрн' in event["request"]["command"].lower()
            or 'black' in event["request"]["command"].lower()):
        return config.get_config_user_move_second(lang)

    return config.get_config_choose_color(lang)
