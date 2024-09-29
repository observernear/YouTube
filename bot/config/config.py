from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Получать тут https://my.telegram.org/auth
    API_ID: int = 21312
    API_HASH: str = "Example_hash"

    # Настройки бота
    # Время между циклами(Чтобы не забанило). Можно оставить без изменения
    SLEEP_TIME: list[int] = [2700, 4200]
    # Задержка перед началом
    START_DELAY: list[int] = [5, 100]
    # Выполнять ли таски автоматически
    AUTO_TASK: bool = True
    # не трогать
    TASKS_TO_DO: list[str] = ["paint20pixels", "x:notpixel", "x:notcoin", "channel:notcoin", "channel:notpixel_channel"]
    # Автоматически ставить пиксели
    AUTO_DRAW: bool = True
    # Разрешить Автоматическую подписку на каналы для выполнения заданий
    JOIN_TG_CHANNELS: bool = True
    # Автоматически Собирать намайненые награды
    CLAIM_REWARD: bool = True
    # Автоматически обновлять бусты
    AUTO_UPGRADE: bool = True
    # не трогать
    IGNORED_BOOSTS: list[str] = ['paintReward']
    IN_USE_SESSIONS_PATH: str = 'bot/config/used_sessions.txt'
    NIGHT_MODE: bool = True
    # Время когда бот должен спать(анти бан). Можно оставить без изменения(Время указано в формате UTC)
    NIGHT_TIME: list[int] = [0, 7]
    # не трогать
    NIGHT_CHECKING: list[int] = [3600, 7200]


settings = Settings()
