import requests
from datetime import datetime
import threading


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

body = {
    "meta": {
        "locale": "ru-RU",
        "timezone": "UTC",
        "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
        "interfaces": {
        "screen": {},
        "payments": {},
        "account_linking": {}
        }
    },
    "session": {
        "message_id": 0,
        "session_id": "bd63eea0-3ff3-45f7-aaf4-246aed08d11f",
        "skill_id": "43e4230e-c63a-4a78-9c96-7e5d9f1c0962",
        "user": {
        "user_id": "A0D70B1AC6713BB0523F0F29EF560EBB8B513588236761A6FD0DD148317FFE31"
        },
        "application": {
        "application_id": "1ABB189FB2D010390956DA7B96C3F8D5C60C75CEED6CEFE358C86FE947DD9585"
        },
        "user_id": "1ABB189FB2D010390956DA7B96C3F8D5C60C75CEED6CEFE358C86FE947DD9585",
        "new": True
    },
    "request": {
        "command": "",
        "original_utterance": "",
        "nlu": {
        "tokens": [],
        "entities": [],
        "intents": {}
        },
        "markup": {
        "dangerous_context": False
        },
        "type": "SimpleUtterance"
    },
    "state": {
        "session": {},
        "user": {},
        "application": {}
    },
    "version": "1.0"
}

def asd():
    startTime = datetime.now()
    res = requests.post('https://ssdteam.ru:2083/', json=body)
    endTime=datetime.now()
    print('Time: ' + str(endTime - startTime))
    print(res)

set_interval(asd, 0.5)
