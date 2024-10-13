# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "22836334"))
API_HASH = getenv("API_HASH", "072b12319aa045abd8710bd92eafbf4b")
BOT_TOKEN = getenv("BOT_TOKEN", "7617250222:AAH6Hwu0ST0MAQItKWRVr12Gxx6o1zhM1cM")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7308378079").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://abayedrisemmons:zh0qKvRKtatgdSmV@cluster0.ct8gs.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP = getenv("LOG_GROUP", "1002265762140")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002265762140"))
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002265762140"))
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "")
