import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", "a71c2aa4f6b764734411512973e34763")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7324735835:AAFpP8QrEvoVc0cGsHqOBBssxNt-E2PIpPQ")
    TELEGRAM_API = os.environ.get("TELEGRAM_API", "22353942")
    OWNER = os.environ.get("OWNER", "6643388068")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "Nordbotzowner")
    PASSWORD = os.environ.get("PASSWORD", "AS_1718")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Merge1:Merge@cluster0.k7ungxs.mongodb.net/")
    LOGCHANNEL = os.environ.get("LOGCHANNEL", "-1002103675380")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BAF7CwcAfZvAxIC-1qGUl6nqJ2ng0KGNXqUIl_kqErXZMFmz0VxbE3qK_vggveVYhefZBYvpHRPyQeCy_ezkcQp4WunWTSrZ7793G4jTIBbObkoS8X0GTt4ol0gQFCsbWXnwbyjJvAkBjIHT8nIwOlT0kcGKh57bTNQTPbHeMgW9n-OhEf_vieKV_PFZbS_btRsDyDp7G6gx_d4sRA5FqkVTQqDLJzY2JdNC90GuXqsqvbY1Yh1tqGvJOCGBLsyXICLGm7UI_03ZN8M2QPQXi7qNe1ppHv8IVzJefOHS8pI5fbFpBmJ47TAAipNz86AORBJm0ziBuJI_xvlrYtKzBWsrbbyuHwAAAAEuadDiAA")
    IS_PREMIUM = True
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
