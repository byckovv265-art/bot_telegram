from pydantic_settings import SettingsConfigDict, BaseSettings
from pydantic import field_validator
from typing import List

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra='ignore',
        env_file='.env'
    )
    TELEGRAM_TOKEN: str = ''
    ADMIN_CHAT_ID: str = ''


settings = Settings()
print(settings.ADMIN_CHAT_ID)
