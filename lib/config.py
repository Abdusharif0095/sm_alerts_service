import os
from dotenv import load_dotenv
from configparser import ConfigParser


load_dotenv(dotenv_path='lib/configs.env')


class Settings:
    PROJECT_NAME: str = "SM Alerts Service"
    PROJECT_VERSION: str = "2.1.0"

    ALERTS_TOPIC: str = os.getenv("ALERTS_TOPIC")
    KAFKA_BROKER: str = os.getenv("KAFKA_BROKER", "localhost:9092")
    KAFKA_GROUP_ID: str = os.getenv("KAFKA_GROUP_ID")
    
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT"))
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_NAME: str = os.getenv("DB_NAME")

    TELEGRAM_TOKEN: str = os.getenv("TELEGRAM_TOKEN")
    TELEGRAM_CHAT_IDS: list[str] = os.getenv("TELEGRAM_CHAT_IDS").split(',')

    DB_ERROR: dict = {
        "tj": os.getenv("DB_ERROR_TJ"),
        "ru": os.getenv("DB_ERROR_RU"),
        "en": os.getenv("DB_ERROR_EN")
    }
    SYSTEM_ERROR: dict = {
        "tj": os.getenv("SYSTEM_ERROR_TJ"),
        "ru": os.getenv("SYSTEM_ERROR_RU"),
        "en": os.getenv("SYSTEM_ERROR_EN")
    }


settings = Settings()
