import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env_bot')

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
weather_api_host = os.getenv("WEATHER_API_HOST")
weather_api_port = os.getenv("WEATHER_API_PORT")
