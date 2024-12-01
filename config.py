import os
from dotenv import load_dotenv

load_dotenv() # get .env

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = os.getenv("API_URL")

X_RAPIADI_KEY = os.getenv("X_RAPIADI_KEY")
X_RAPIADI_HOST = os.getenv("X_RAPIADI_HOST")
