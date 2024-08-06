import os


class Config(object):
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    TELEGRAM_API = os.environ.get("TELEGRAM_API")
    OWNER = os.environ.get("OWNER", "6643388068")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
    PASSWORD = os.environ.get("PASSWORD", "AS_1718")
    DATABASE_URL = os.environ.get("DATABASE_URL")
    LOGCHANNEL = os.environ.get("LOGCHANNEL")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING")
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
