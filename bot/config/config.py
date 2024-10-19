from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
#API_ID и API_HASH
    API_ID: int = 12
    API_HASH: str = "daw"
#Миниму доступной энергии
    MIN_AVAILABLE_ENERGY: int = 300
#Столько времени ждем для восстановления энергии
    SLEEP_BY_MIN_ENERGY: int = 311
# Сколько нажатий будет при активации турбо
    ADD_TAPS_ON_TURBO: list[int] = [500, 1500]
# Покупать бота?
    AUTO_BUY_TAPBOT: bool = True
#Стоит ли улучшать тапы
    AUTO_UPGRADE_TAP: bool = False
#Макс уровень тапов
    MAX_TAP_LEVEL: int = 5
#Стоит ли улучшать энергию
    AUTO_UPGRADE_ENERGY: bool = False
#Макс уровень энергии    
    MAX_ENERGY_LEVEL: int = 5
#Стоит ли улучшать перезарядку
    AUTO_UPGRADE_CHARGE: bool = False
#Макс уровень перезарядки    
    MAX_CHARGE_LEVEL: int = 3
#Использовать ли ежедневный бесплатный заряд энергии
    APPLY_DAILY_ENERGY: bool = True
#Использовать ли ежедневный бесплатный турбо
    APPLY_DAILY_TURBO: bool = True
#Сколько нажатий будет
    RANDOM_TAPS_COUNT: list[int] = [7, 31]
#Сколько времени ждем между нажатиями
    SLEEP_BETWEEN_TAP: list[int] = [19, 36]
#Использовать ли прокси из файла bot/config/proxies.txt
    USE_PROXY_FROM_FILE: bool = False
#Срочная остановска(ЛУЧШЕ НЕ ТРОГАТЬ)
    EMERGENCY_STOP: bool = False
#Играть ли в казино
    ROLL_CASINO: bool = True
#Количество спинов
    VALUE_SPIN: int = 10
#Играть ли в лотерею
    LOTTERY_INFO: bool = True

#Будет ли использоваться рандомная задержка перед запуском
    USE_RANDOM_DELAY_IN_RUN: bool = True
#Задержка перед запуском
    RANDOM_DELAY_IN_RUN: list[int] = [3, 15]


settings = Settings()
