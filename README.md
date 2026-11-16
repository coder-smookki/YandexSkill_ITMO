<h1 align="center">ИТМО Помощник</h1>

<p align="center">
  <img alt="Навык Алисы" src="https://img.shields.io/badge/%D0%BD%D0%B0%D0%B2%D1%8B%D0%BA-%D0%90%D0%BB%D0%B8%D1%81%D1%8B-8100FF?style=for-the-badge">
  <img alt="Хакатон Алисы и ИТМО 2023" src="https://img.shields.io/badge/%D1%85%D0%B0%D0%BA%D0%B0%D1%82%D0%BE%D0%BD-%D0%90%D0%BB%D0%B8%D1%81%D1%8B%20%D0%B8%20%D0%98%D0%A2%D0%9C%D0%9E%202023-FC3F1D?style=for-the-badge">
  <img alt="Русский и английский" src="https://img.shields.io/badge/%D1%8F%D0%B7%D1%8B%D0%BA%D0%B8-RU%20%C2%B7%20EN-121316?style=for-the-badge">
  <br>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10-3776AB?style=flat-square&logo=python&logoColor=white">
  <img alt="Flask" src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white">
  <img alt="Beautiful Soup" src="https://img.shields.io/badge/Beautiful%20Soup-4-3776AB?style=flat-square">
  <img alt="Requests" src="https://img.shields.io/badge/Requests-3776AB?style=flat-square">
  <img alt="num2words" src="https://img.shields.io/badge/num2words-3776AB?style=flat-square">
  <img alt="SQLite" src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white">
  <img alt="Яндекс Диалоги" src="https://img.shields.io/badge/%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81-%D0%94%D0%B8%D0%B0%D0%BB%D0%BE%D0%B3%D0%B8-FC3F1D?style=flat-square">
  <a href="#лицензия"><img alt="Лицензия MIT" src="https://img.shields.io/badge/%D0%BB%D0%B8%D1%86%D0%B5%D0%BD%D0%B7%D0%B8%D1%8F-MIT-2EA043?style=flat-square"></a>
</p>

<p align="center">
  Навык Алисы для студентов Университета ИТМО: новости и анонсы с сайта университета, расписание занятий группы, поиск учебных и методических изданий, ответы студенческого офиса, советы первокурсникам и иностранным студентам, стипендии, а также шахматы, викторина и случайные факты. Работает на русском и английском языках
</p>

<p align="center">
  <a href="#что-умеет-навык"><b>Что умеет</b></a> ·
  <a href="#как-устроен-навык"><b>Как устроен</b></a> ·
  <a href="#быстрый-старт"><b>Быстрый старт</b></a> ·
  <a href="#команда"><b>Команда</b></a> ·
  <a href="#хакатон"><b>Хакатон</b></a>
</p>

Навык создан на хакатоне Алисы и ИТМО по разработке приложений для голосовых ассистентов в 2023 году. Фраза запуска: «Алиса, запусти навык ИТМО Помощник». Сейчас навык не размещён на сервере и не работает.

## Что умеет навык

| Раздел | Что внутри |
|---|---|
| Новости | Категории «Анонсы» и «Контесты» с `news.itmo.ru`, обновляются раз в час |
| Расписание занятий | Расписание вашей группы со `student.itmo.ru` |
| Учебные и методические издания | Поиск изданий в каталоге `books.ifmo.ru` |
| Студенческий офис | Ответы на частые вопросы студентов |
| Первокурсникам | Полезная информация для первокурсников |
| Общеуниверситетские модули | Модули бакалавриата и магистратуры |
| Иностранному студенту | Частые вопросы иностранных студентов: документы, бакалавриат, магистратура и другое |
| Библиотека | Возможности библиотеки университета |
| Стипендии | Информация о стипендиях и их категориях |
| Шахматы | Партия в шахматы голосом: ходы в формате «клетка-клетка», например e2e4 или e2-e4, на устройствах с экраном доска приходит картинкой |
| Викторина | Вопросы по математике, информационным технологиям и другим областям |
| Случайный факт | Факты об окружающем мире и ИТМО |

Везде доступны «Помощь», «Повторить ещё раз», «Что ты умеешь?», «Назад» и «Выйти», язык меняется кнопкой «Сменить язык».

## Как устроен навык

| Что | Где |
|---|---|
| Flask-сервер: принимает POST-запросы Алисы, проверяет `skill_id`, выбирает диалог, раз в час обновляет новости в фоне | [src/backend/index.py](src/backend/index.py) |
| Диалоги всех разделов, у каждого `config.py` с текстами на русском и английском | [src/backend/dialogs/](src/backend/dialogs) |
| Парсер сайтов ИТМО на Beautiful Soup: анонсы, контесты, издания, группы и расписание | [src/backend/utils/parser/](src/backend/utils/parser) |
| Шахматы: доска в SQLite, картинки доски загружаются в Яндекс Диалоги | [src/backend/dialogs/chessGame/](src/backend/dialogs/chessGame) |
| Вопросы викторины | [src/backend/questions.json](src/backend/questions.json) |
| Запуск через gunicorn в цикле с `git pull` | [src/backend/start.sh](src/backend/start.sh) |

Ходы шахматной партии обрабатывает отдельный шахматный API по адресу `http://127.0.0.1:5000/api/chess/`, его кода в этом репозитории нет.

## Быстрый старт

Сначала создайте навык в [Яндекс Диалогах](https://dialogs.yandex.ru/developer).

```sh
git clone https://github.com/coder-smookki/YandexSkill_ITMO.git
cd YandexSkill_ITMO
python -m venv .venv
pip install -r requirements.txt
cd src/backend
python index.py
```

Код также импортирует `python-dotenv` и `Pillow`, которых нет в `requirements.txt`: установите их отдельно. Файл `.env` создайте сами в `src/backend`:

| Переменная | Назначение |
|---|---|
| `SKILL_ID` | Идентификатор навыка: запросы от других навыков отклоняются |
| `OAUTH_IMAGE_KEY` | OAuth-токен Яндекс Диалогов для загрузки картинок шахматной доски |

Сервер слушает `0.0.0.0:2083` и принимает запросы Алисы методом POST по адресу `/`.

## Команда

Состав взят из раздела навыка «Кто создатели навыка?» ([src/backend/dialogs/whoIsCreator/config.py](src/backend/dialogs/whoIsCreator/config.py)).

| Участник | Роль | GitHub |
|---|---|---|
| Ильин Кирилл | Тимлид | [@coder-smookki](https://github.com/coder-smookki) |
| Плюснин Александр | Главный разработчик навыка и его основы | [@elogrus](https://github.com/elogrus) |
| Караваев Иван | Разработчик | [@Nauryeasy](https://github.com/Nauryeasy) |
| Лесовой Кирилл | Тестировщик, разработчик игровых алгоритмов | [@K1rL3s](https://github.com/K1rL3s) |
| Кутников Родион | Главный дизайнер, UI и UX | |

## Хакатон

<p align="center">
  <img src="screenshots/image.png" alt="Хакатон Алисы и ИТМО по разработке приложений для голосовых ассистентов" width="520">
</p>

## Лицензия

Код распространяется под лицензией MIT, полный текст - в [LICENSE](LICENSE).
