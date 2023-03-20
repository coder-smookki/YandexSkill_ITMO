import requests


class Translater:
    def __init__(self, IAM_TOKEN, folder_id):
        self.target_language = 'ru'
        self.source_language = 'en'
        self.IAM_TOKEN = IAM_TOKEN
        self.folder_id = folder_id
        self.body = {
            "targetLanguageCode": self.target_language,
            "folderId": folder_id
        }
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {0}".format(IAM_TOKEN)
        }

    def translate(self, text):
        self.body["texts"] = text.split()
        response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate', json=self.body, headers=self.headers)
        return response

    # def translate(self, text):
    #     pattern = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&text={}&lang={}'
    #     direction = self.source_language + '-' + self.target_language
    #     req = pattern.format(self.IAM_TOKEN, text, direction)
    #     resp = requests.get(req)
    #     if resp.status_code != 200:
    #         return 'Не достучалась до переводчика. ' + req, ''
    #
    #     j = json.loads(resp.text)
    #     return None, j['text'][0]

translater = Translater("t1.9euelZqMyJ7Oz5nPjJWQzIqOkJGbz-3rnpWal82VjcySyJTOkMqOjc6LzYrl9PcYIi1f-e85UlbG3fT3WFAqX_nvOVJWxg.fbuqAcUXxKRgrXItMmTbNhW0gI0mxDY46LZYxgfTSS8XiQK4X1vhWC5fZ5ITOU8bBOa6MlBSKL9G-RK4ZLyvDw", "d4egunb77s46bi3269ng")
print(translater.translate('Hello world').content)
