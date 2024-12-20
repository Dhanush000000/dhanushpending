from os import environ

API_ID = int(environ.get("API_ID", "20389440"))
API_HASH = environ.get("API_HASH", "a1a06a18eb9153e9dbd447cfd5da2457")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", ""))
ADMINS = int(environ.get("ADMINS", "5798247275"))
DB_URI = environ.get("DB_URI", "mongodb+srv://dhanush1236:dhanush1236@cluster0.gxssv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")
