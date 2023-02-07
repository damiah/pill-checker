import sys
import logging

from loguru import logger
from starlette.config import Config
from starlette.datastructures import Secret

from core.logging import InterceptHandler

config = Config(".env")

API_PREFIX = "/api"
VERSION = "0.1.0"
DEBUG: bool = config("DEBUG", cast=bool, default=False)
MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT", cast=int, default=10)
MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT", cast=int, default=10)
SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret, default="")

PROJECT_NAME: str = config("PROJECT_NAME", default="pill-checker")

# logging configuration
LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
logging.basicConfig(
    handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL
)
logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])

CROPPED_PILL_PATH = "./static/images/cropped/"
UPLOADED_PILL_PATH = "./static/images/uploads/"
PILL_INFO = "./static/pill_info/pill_info.pkl"
PILL_INFO_URL = "https://knowyourstuff.nz/pill-library/"
MODEL_PATH = "./static/models/transformer_model.pkl"