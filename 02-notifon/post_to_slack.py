# coding: utf-8
import requests
url = 'https://hooks.slack.com/services/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' # Replace with slack webhook URL
data = { "text": "Hello, world." }
requests.post(url, json=data)
