import requests
import config as cfg
from time import sleep
from pprint import pprint


response = requests.post(url='https://pay.ton-rocket.com/tg-invoices', headers={'Rocket-Pay-Key': "YOUR_API"}, json={
    "amount": 1,
    "currency": "USDT",
    "description": "Test invoice",
    "hiddenMessage": "thank you",
    "commentsEnabled": False,
    "expiredIn": 300})
pprint(response.json())
id = (response.json())['data']['id']
link = (response.json())['data']['link']
print(id, link, sep='\n')


while True:
    response = requests.get(
        url=f'https://pay.ton-rocket.com/tg-invoices/{id}', headers={'Rocket-Pay-Key': "YOUR_API"})
    status = (response.json())['data']['status']
    pprint.pprint(response.json())
    if status == 'paid':
        break
    sleep(1)
