import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_BASE_URL = os.getenv(key='APP_BASE_URL', default=None)


settings = Settings()
