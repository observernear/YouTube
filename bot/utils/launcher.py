<<<<<<< HEAD
import os
import glob
import asyncio
import argparse
from itertools import cycle

from pyrogram import Client
=======
import asyncio
import argparse
from random import randint
from typing import Any
>>>>>>> 25aba28 (edit proxy)
from better_proxy import Proxy

from bot.config import settings
from bot.utils import logger
from bot.core.tapper import run_tapper
<<<<<<< HEAD
from bot.core.registrator import register_sessions

start_text = """

███╗   ██╗ ██████╗ ████████╗██████╗ ██╗██╗  ██╗███████╗██╗
████╗  ██║██╔═══██╗╚══██╔══╝██╔══██╗██║╚██╗██╔╝██╔════╝██║
██╔██╗ ██║██║   ██║   ██║   ██████╔╝██║ ╚███╔╝ █████╗  ██║
██║╚██╗██║██║   ██║   ██║   ██╔═══╝ ██║ ██╔██╗ ██╔══╝  ██║
██║ ╚████║╚██████╔╝   ██║   ██║     ██║██╔╝ ██╗███████╗███████╗
╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝

Select an action:

    1. Start drawing 🎨️
    2. Create a session 👨‍🎨

"""

global tg_clients


def get_session_names() -> list[str]:
    session_names = sorted(glob.glob("sessions/*.session"))
    session_names = [
        os.path.splitext(os.path.basename(file))[0] for file in session_names
    ]

    return session_names


def get_proxies() -> list[Proxy]:
    if settings.USE_PROXY_FROM_FILE:
        with open(file="bot/config/proxies.txt", encoding="utf-8-sig") as file:
            proxies = [Proxy.from_str(proxy=row.strip()).as_url for row in file]
    else:
        proxies = []

    return proxies


async def get_tg_clients() -> list[Client]:
    global tg_clients

    session_names = get_session_names()

    if not session_names:
        raise FileNotFoundError("Not found session files")

    if not settings.API_ID or not settings.API_HASH:
        raise ValueError("API_ID and API_HASH not found in the .env file.")

    tg_clients = [
        Client(
            name=session_name,
            api_id=settings.API_ID,
            api_hash=settings.API_HASH,
            workdir="sessions/",
            plugins=dict(root="bot/plugins"),
        )
        for session_name in session_names
    ]

    return tg_clients
=======
from bot.core.registrator import register_sessions, get_tg_client
from bot.utils.accounts import Accounts
from bot.utils.firstrun import load_session_names

art_work = """

888b    888          888    8888888b.  d8b                   888 
8888b   888          888    888   Y88b Y8P                   888 
88888b  888          888    888    888                       888 
888Y88b 888  .d88b.  888888 888   d88P 888 888  888  .d88b.  888 
888 Y88b888 d88""88b 888    8888888P"  888 `Y8bd8P' d8P  Y8b 888 
888  Y88888 888  888 888    888        888   X88K   88888888 888 
888   Y8888 Y88..88P Y88b.  888        888 .d8""8b. Y8b.     888 
888    Y888  "Y88P"   "Y888 888        888 888  888  "Y8888  888                                    
"""

version = "v3.0.1"

start_text = """                                             
Выбери действие:
    1. Запуск
    2. Создать сессию
"""


def get_proxy(raw_proxy: str) -> Proxy:
    return Proxy.from_str(proxy=raw_proxy).as_url if raw_proxy else None
>>>>>>> 25aba28 (edit proxy)


async def process() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--action", type=int, help="Action to perform")
<<<<<<< HEAD

    logger.info(f"Detected {len(get_session_names())} sessions | {len(get_proxies())} proxies")

    action = parser.parse_args().action

    if not action:
=======
    action = parser.parse_args().action

    if not action:
        print('\033[1m' + '\033[92m' + art_work + '\033[0m')
        print('\033[1m' + '\033[93m' + version + '\033[0m')

        #if settings.AUTO_TASK:
            #logger.warning("Auto Task is enabled, it is dangerous functional")

>>>>>>> 25aba28 (edit proxy)
        print(start_text)

        while True:
            action = input("> ")

            if not action.isdigit():
<<<<<<< HEAD
                logger.warning("Action must be number")
            elif action not in ["1", "2"]:
                logger.warning("Action must be 1 or 2")
=======
                logger.warning("Ты ввел не число")
            elif action not in ["1", "2"]:
                logger.warning("вводи 1 или 2")
>>>>>>> 25aba28 (edit proxy)
            else:
                action = int(action)
                break

<<<<<<< HEAD
    if action == 1:
        tg_clients = await get_tg_clients()

        await run_tasks(tg_clients=tg_clients)

    elif action == 2:
        await register_sessions()

async def run_tasks(tg_clients: list[Client]):
    proxies = get_proxies()
    proxies_cycle = cycle(proxies) if proxies else None
    tasks = [
        asyncio.create_task(
            run_tapper(
                tg_client=tg_client,
                proxy=next(proxies_cycle) if proxies_cycle else None,
            )
        )
        for tg_client in tg_clients
    ]
=======
    used_session_names = load_session_names()

    if action == 2:
        await register_sessions()
    elif action == 1:
        accounts = await Accounts().get_accounts()
        await run_tasks(accounts=accounts, used_session_names=used_session_names)


async def run_tasks(accounts: [Any, Any, list], used_session_names: [str]):
    tasks = []
    for account in accounts:
        session_name, user_agent, raw_proxy = account.values()
        first_run = session_name not in used_session_names
        tg_client = await get_tg_client(session_name=session_name, proxy=raw_proxy)
        proxy = get_proxy(raw_proxy=raw_proxy)
        tasks.append(asyncio.create_task(run_tapper(tg_client=tg_client, proxy=proxy)))
        await asyncio.sleep(randint(5, 20))
>>>>>>> 25aba28 (edit proxy)

    await asyncio.gather(*tasks)
