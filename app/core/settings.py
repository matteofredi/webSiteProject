import ast
import os
from typing import List

from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_BASE_URL: str = os.getenv(key='APP_BASE_URL', default=None)
    ALLOWED_HOST: List[str] = ast.literal_eval(os.getenv(key='ALLOWED_HOST', default=None))


settings = Settings()
