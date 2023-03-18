import os
import sqlite3
from threading import Timer
from io import BytesIO

import requests
from PIL import Image
from dotenv import dotenv_values

env_vars = dotenv_values(".env")
oauth_key = env_vars.get("OAUTH_IMAGE_KEY")
skill_id = env_vars.get("SKILL_ID")
api_base = 'http://127.0.0.1:5000/api/chess/'
url = f'https://dialogs.yandex.net/api/v1/skills/{skill_id}/images/'

big_width, big_height = 776, 344
small_width, small_height = 388, 172


def create_db():
    conn = sqlite3.connect('chess.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "boards" (
        "id" INTEGER NOT NULL UNIQUE,
        "fen" TEXT NOT NULL,
        "orientation" TEXT NOT NULL,
        "last_move" TEXT NOT NULL,
        "check_square" TEXT,
        "image_id" TEXT NOT NULL UNIQUE,
        PRIMARY KEY("id" AUTOINCREMENT)
    )''')
    conn.commit()

    cursor.execute("DELETE board")
    conn.commit()

    conn.close()


def redo_image(image: bytes) -> bytes:
    image = Image.open(BytesIO(image), mode='r')
    background = Image.new("RGB", (big_width, big_height), (0, 0, 0))
    background.paste(image, ((big_width - big_height) // 2, 0))

    img_byte_arr = BytesIO()
    background.save(img_byte_arr, format='PNG')

    return img_byte_arr.getvalue()


def cache_new_board_id(fen: str, orientation: str, last_move: str, check: str) -> str | None:
    params = {
        "fen": fen,
        "orientation": orientation,
        "last_move": last_move,
        "check": check,
        "size": big_height
    }
    board_response = requests.get(api_base + 'board', params=params)
    if board_response.status_code != 200:  # Либо сервер сломался, либо неверные параметры в ходе игры.
        return None

    headers = {
        "Authorization": f'OAuth {oauth_key}',
    }
    yandex_response = requests.post(url,
                                    headers=headers,
                                    files={'file': redo_image(board_response.content)})

    if yandex_response.status_code == 429:  # Обработка момента, когда занята вся память навыка (около 2к картинок)
        raise RuntimeError("Киря, бачок потик, места нема!!! КАРТИНОК БОЛЬШЕ СТА МЕГАБАЙТ")

    if not yandex_response:
        print(f'Возникла ошибка {yandex_response.status_code} "{yandex_response.text}"')
        return None
    image_id = yandex_response.json()["image"]["id"]

    conn = sqlite3.connect('chess.db')
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO boards (fen, orientation, last_move, check_square, image_id) values (?, ?, ?, ?, ?)
    """, (fen, orientation, last_move, check or 0, image_id))
    conn.commit()

    return image_id


def get_board_id(fen: str, orientation: str, last_move: str, check: str | None) -> str:
    conn = sqlite3.connect('chess.db')
    cursor = conn.cursor()

    board_id = cursor.execute("""
    SELECT image_id FROM boards WHERE fen = ? AND orientation = ? AND last_move = ? AND check_square = ?
    """, (fen, orientation, last_move, check or 0)).fetchone()
    if not board_id:
        board_id = [cache_new_board_id(fen, orientation, last_move, check)]
    board_id = board_id[0]
    del_thread = Timer(60, delete_board_id, args=(board_id,))
    del_thread.start()
    return board_id


def delete_board_id(image_id: str):
    conn = sqlite3.connect('chess.db')
    cursor = conn.cursor()
    cursor.execute("""
    DELETE FROM boards WHERE image_id = ?
    """, (image_id,))
    conn.commit()

    headers = {
        "Authorization": f'OAuth {oauth_key}',
    }
    yandex_response = requests.delete(url + image_id, headers=headers)
    if not yandex_response:
        print(f'Не удалось удалить image {image_id}\n{yandex_response.text}')


create_db()
