import requests
import config as cfg
response = requests.post(url='https://pay.ton-rocket.com/multi-cheque', headers={'Rocket-Pay-Key': "YOUR_API"}, json={
    "currency": "USDT",
    "chequePerUser": 1,
    "usersNumber": 1,
    "refProgram": 0,
    "description": "Test description",
    "sendNotifications": True,
    "enableCaptcha": False,
    "forPremium": False,
    "linkedWallet": False,
})
link = (response.json())['data']['link']
print(link)
