from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    #api id и api hash
    API_ID: int = 2131
    API_HASH: str = "dawd"

# использовать ли прокси из файла proxies.txt
    USE_PROXY_FROM_FILE: bool = False

#кликов за раз
    TAPS: list = [10, 100] 
#задержка между кликами    
    SLEEP_BETWEEN_TAPS: list = [1, 3] 
#минимум доступной энергии
    ENERGY_THRESHOLD: float = 0.05
#задержка когда энергия кончилась
    SLEEP_ON_LOW_ENERGY: int = 60 * 15
#задержка после улучшения    
    SLEEP_AFTER_UPGRADE: int = 1
#задержка между заданиями
    DELAY_BETWEEN_TASKS: list = [3, 15]
# задержка между проверкой обновлений
    UPGRADE_CHECK_DELAY: int = 60
# задержка между попыткой обновиться
    RETRY_DELAY: int = 3
# максимальное количество попыток выполнить задачу в случае ошибки
    MAX_RETRIES: int = 5

# включить/отключить клики
    ENABLE_TAPS: bool = True
# включить/отключить сбор 
    ENABLE_CLAIM_REWARDS: bool = True
# включить/отключить обновления
    ENABLE_UPGRADES: bool = True
# включить/отключить задания
    ENABLE_TASKS: bool = True

    @property
    def MIN_TAPS(self):
        return self.TAPS[0]

    @property
    def MAX_TAPS(self):
        return self.TAPS[1]

    @property
    def MIN_SLEEP_BETWEEN_TAPS(self):
        return self.SLEEP_BETWEEN_TAPS[0]

    @property
    def MAX_SLEEP_BETWEEN_TAPS(self):
        return self.SLEEP_BETWEEN_TAPS[1]

    @property
    def MIN_DELAY_BETWEEN_TASKS(self):
        return self.DELAY_BETWEEN_TASKS[0]

    @property
    def MAX_DELAY_BETWEEN_TASKS(self):
        return self.DELAY_BETWEEN_TASKS[1]

settings = Settings()
