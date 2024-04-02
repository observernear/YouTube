import requests
from pprint import pprint

response = requests.get(url='https://pay.ton-rocket.com/app/info',
                        headers={'Rocket-Pay-Key': "YOUR_API"})
pprint(response.json())
