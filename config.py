import os

class Config:
    API_ID = os.environ.get("API_ID", "")
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    REDIS_URI = os.environ.get("REDIS_URL", "") # Heroku Redis URL
    REDIS_PORT = os.environ.get("REDIS_PORT", "")
    REDIS_PASS = os.environ.get("REDIS_PASS", "")
    OWNER = os.environ.get("OWNER", "")  # Bot owner's username

