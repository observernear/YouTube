import requests
import schedule
import time
from random import randint


from work_token import refresh_token


with open('tokens.txt') as f:
    TOKENS = f.read().splitlines()

get_balance = 'https://game-domain.blum.codes/api/v1/user/balance'
get_tasks = 'https://game-domain.blum.codes/api/v1/tasks'
get_frens = 'https://game-domain.blum.codes/api/v1/friends'
post_claim = 'https://game-domain.blum.codes/api/v1/farming/claim'
post_start = 'https://game-domain.blum.codes/api/v1/farming/start'


def job():
    for token in TOKENS:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Authorization': f'Bearer {token}', 
            'refresh': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJoYXNfZ3Vlc3QiOmZhbHNlLCJ0eXBlIjoiUkVGUkVTSCIsImlzcyI6ImJsdW0iLCJzdWIiOiI5ODhjZDczNS1hOTA4LTRhY2QtOTQyZS00NTUyYWJiMjQyYjUiLCJleHAiOjE3MTUzODcyMDAsImlhdCI6MTcxNTMwMDgwMH0.v9bYXNnEL3yH3WKh_-Nrg1rVID7ELiHBJRQSa5At4G0',
            'Origin': 'https://telegram.blum.codes',
            'Referer': 'https://telegram.blum.codes/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site'
        }

        response1 = requests.post(post_claim, headers=headers)
        time_ = randint(3, 6)
        time.sleep(time_)
        response2 = requests.post(post_start, headers=headers)

        print(f'\nStatus 1: {response1.status_code}\nJson: {response1.json()}\n\nStatus 2: {response2.status_code}\nJson: {response2.json()}')

job()
schedule.every(8).hours.do(job)

while True:
    for index in range(len(TOKENS)):
        time.sleep(2)
        new_token = refresh_token(TOKENS[index])
        TOKENS[index] = new_token

    with open('tokens.txt', 'w') as f:
        for token in TOKENS:
            f.write(f'{token}\n')
    schedule.run_pending()
    time.sleep(2)

