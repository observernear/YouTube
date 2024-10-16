import sqlite3
import os
from telethon import TelegramClient
from telethon.sessions import SQLiteSession
from telethon.crypto import AuthKey  # Импортируем AuthKey
from bot.config import settings

# Параметры API, которые вам нужно будет указать
API_ID = settings.API_ID
API_HASH = settings.API_HASH

def convert_pyrogram_to_telethon():
    sessions = os.walk("pyro_to_telethon")
    sessions = sessions.__next__()[2]
    for session in sessions:
        pyrogram_session_path = f"pyro_to_telethon/{str(session)}"
        telethon_session_path = f'sessions/{str(session).replace(".session", "_telethon.session")}'
        print(f"Converting {pyrogram_session_path} to {telethon_session_path}...")
        # Проверка на существование файла сессии Pyrogram
        if not os.path.exists(pyrogram_session_path):
            raise FileNotFoundError(f"Pyrogram session file not found: {pyrogram_session_path}")

        # Открытие базы данных Pyrogram
        conn = sqlite3.connect(pyrogram_session_path)
        cursor = conn.cursor()

        # Проверяем структуру таблицы
        cursor.execute("PRAGMA table_info(sessions)")
        columns = cursor.fetchall()

        # Извлечение данных из Pyrogram-сессии (скорректируйте запрос под вашу схему)
        cursor.execute("SELECT dc_id, auth_key, user_id FROM sessions LIMIT 1")
        result = cursor.fetchone()

        if result is None:
            raise Exception("No session data found in Pyrogram session file.")

        dc_id, auth_key, user_id = result

        # Закрытие соединения с базой данных
        conn.close()

        # Преобразование auth_key из байтов в объект AuthKey
        auth_key = AuthKey(data=auth_key)

        # Создание новой сессии Telethon
        telethon_session = SQLiteSession(telethon_session_path)
        
        client = TelegramClient(telethon_session, API_ID, API_HASH)

        # Устанавливаем данные дата-центра с помощью метода set_dc
        telethon_session.set_dc(dc_id, '149.154.167.50', 443)  # Пример IP и порта; измените при необходимости
        telethon_session.auth_key = auth_key
        telethon_session.save()

        client.connect()

        print(f"Telethon session saved to {telethon_session_path}")