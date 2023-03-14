import pytest
import json
from pathlib import Path

from src.backend.dialogs.chessGame.event_handler import event_handler


with open(Path().absolute() / 'configs.json', 'r', encoding='utf-8') as f:
    configs = json.load(f)


def test_event_handler1():
    event = configs["1"]
    answer = event_handler(event)
    assert answer == {'e2', 'e4'}


def test_event_handler2():
    event = configs["2"]
    answer = event_handler(event)
    assert answer == {"d4", "g3", "e7", "e5", "e7", "e8"}
