import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "7591126816:AAG3XXGZUXkIFUkK4Qtu6uD2Az3kRLTiP6A")
API_ID = int(os.environ.get("API_ID", "24828197"))
API_HASH = os.environ.get("API_HASH", "d36e278e89ebeb900aeda4128d413a77")


OWNER_ID = int(os.environ.get("OWNER_ID", "7768598381"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://musicbhaikon9910:krishna@cluster0.cwvegmt.mongodb.net/")
JOIN_REQ_DB = os.environ.get("JOIN_REQ_DB", DB_URL)
DB_NAME = os.environ.get("DB_NAME", "Madflix-Files")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002386383823"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002239014353"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "1500")) # auto delete in seconds


PORT = os.environ.get("PORT", "8000")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[7660990923]
    for x in (os.environ.get("ADMINS", "2089948673 2089948673").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "False") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "<b></b>"

START_MSG = os.environ.get("START_MESSAGE", "<b>›› Hᴇʏ {first} × \n     ɪ ᴀᴍ ᴀ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @ADR_ANIME_HINDI ⚡.</b>")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>›› Hᴇʏ {mention} × \n     ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, ᴊᴏɪɴ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs.</b>")





ADMINS.append(OWNER_ID)
ADMINS.append(7660990923)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   


 
# try your best 🥱
# next time 😂😂
