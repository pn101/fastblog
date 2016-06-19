import json
import requests


def slack_notification(username, text):
    BASE_URL = 'https://hooks.slack.com/services/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'
    data_list = {
        'username': username,
        'text': text,
    }
    data_list = json.dumps(data_list)
    response = requests.post(BASE_URL, data_list)
