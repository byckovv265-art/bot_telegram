from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra='ignore',
        env_file='.env'
    )
    TELEGRAM_TOKEN: str = ''
    ADMIN_CHAT_ID: str = ''


settings = Settings()
