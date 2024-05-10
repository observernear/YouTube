import requests

USER_CHECK_URL = "https://gateway.blum.codes/v1/user/me"
REFRESH_TOKEN_URL = "https://gateway.blum.codes/v1/auth/refresh"


def get_headers():
    return {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Origin': 'https://telegram.blum.codes',
    'Referer': 'https://telegram.blum.codes/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'TE': 'trailers'}

def is_token_valid(token):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Authorization': f'Bearer {token}', 
        'Origin': 'https://telegram.blum.codes',
        'Referer': 'https://telegram.blum.codes/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site'
    }
    response = requests.get(USER_CHECK_URL, headers=headers)
    
    if response.status_code == 200:
        return True
    else:
        return False

def refresh_token(refresh_token):
    refresh_payload = {
        'refresh': refresh_token 
    }

    headers = get_headers()

    response = requests.post(
        REFRESH_TOKEN_URL,
        headers = headers,
        json=refresh_payload
    )
    return response.json().get("access")
