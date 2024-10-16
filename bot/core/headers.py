import re


headers = {
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://major.bot',
    'Referer': 'https://major.bot/',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Ch-Ua-Mobile': '?1',
    'Sec-Ch-Ua-Platform': '"Android"',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Priority': 'u=1, i'
}


def get_sec_ch_ua(user_agent):
    pattern = r'(Chrome|Chromium)\/(\d+)\.(\d+)\.(\d+)\.(\d+)'

    match = re.search(pattern, user_agent)

    if match:
        browser = match.group(1)
        version = match.group(2)

        if browser == 'Chrome':
            sec_ch_ua = f'"Chromium";v="{version}", "Not;A=Brand";v="24", "Google Chrome";v="{version}"'
        else:
            sec_ch_ua = f'"Chromium";v="{version}", "Not;A=Brand";v="24"'

        return {'Sec-Ch-Ua': sec_ch_ua}
    else:
        return {}
