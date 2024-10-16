from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    #api_id и api_hash
    API_ID: int = 31231
    API_HASH: str = "12312313"

    #использовать прокси в файле
    USE_PROXY_FROM_FILE: bool = False

    #подписка на каналы в заданиях
    TASKS_WITH_JOIN_CHANNEL: bool = True
    #награда в HoldCoin
    HOLD_COIN: list[int] = [915, 915]
    #награда в SwipeCoin
    SWIPE_COIN: list[int] = [2000, 3000]
    #сквад
    SUBSCRIBE_SQUAD: str = '-1002111853956'
    #использовать случайные задержки в цикле
    USE_RANDOM_DELAY_IN_RUN: bool = True
    #небольшие задержки в цикле
    RANDOM_DELAY_IN_RUN: list[int] = [0, 30]
    #сон после цикла
    SLEEP_TIME: list[int] = [1800, 3600]
    #Количество сессий, которые могут использовать один и тот же прокси
    SESSIONS_PER_PROXY: int = 1
    #Отключить автоматическую проверку и замену нерабочих прокси перед запуском 
    DISABLE_PROXY_REPLACE: bool = False
    
    
    
    #Это лучше не трогать
    USE_PROXY_CHAIN: bool = False

    DEVICE_PARAMS: bool = False

    DEBUG_LOGGING: bool = False

    GLOBAL_CONFIG_PATH: str = "TG_FARM"


settings = Settings()
