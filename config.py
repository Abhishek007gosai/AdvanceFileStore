import logging
from logging.handlers import RotatingFileHandler

# Bot Configuration
LOG_FILE_NAME = "bot.log"
PORT = '5010'
OWNER_ID = 7654385403

MSG_EFFECT = 5046509860389126442

SHORT_URL = "" # shortner url 
SHORT_API = "" 
SHORT_TUT = ""

# Bot Configuration
SESSION = ""
TOKEN = ""
API_ID = ""
API_HASH = ""
WORKERS = 5

DB_URI = ""
DB_NAME = ""

FSUBS = [[-1001457313028, True, 10]] # Force Subscription Channels [channel_id, request_enabled, timer_in_minutes]
# Database Channel (Primary)
DB_CHANNEL =    # just put channel id dont add ""
# Multiple Database Channels (can be set via bot settings)
# DB_CHANNELS = {
#     "-1002595092736": {"name": "Primary DB", "is_primary": True, "is_active": True},
#     "-1001234567890": {"name": "Secondary DB", "is_primary": False, "is_active": True}
# }
# Auto Delete Timer (seconds)
AUTO_DEL = 300
# Admin IDs
ADMINS = [6497757690, 6103092779]
# Bot Settings
DISABLE_BTN = True
PROTECT = False

# Messages Configuration
MESSAGES = {
    "START": "<b><blockquote>Hᴇʏ! {mention} Wᴇʟᴄᴏᴍᴇ Tᴏ Cᴏᴍᴍᴜɴɪᴛʏ Iғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴜᴘᴘᴏʀᴛ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ ʏᴏᴜ ᴄᴀɴ ᴅᴏ sᴏ ʙʏ sᴜʙsᴄʀɪʙɪɴɢ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ</blockquote></a>\n<blockquote expandable></a>Gᴜɪᴅᴇ Tᴏ Wᴀᴛᴄʜ Vɪᴅᴇᴏ Wɪᴛʜ Sᴜʙᴛɪᴛʟᴇs Iғ Sᴜʙᴛɪᴛʟᴇs Nᴏᴛ Sʜᴏᴡɪɴɢ\n</a>❏ ᴛᴜᴛᴏʀɪᴀʟ\n</a>├ <a href=https://telegra.ph/HOW-TO-WATCH-04-20-3>Cʟɪᴄᴋ Hᴇʀᴇ </a>\n❏ Hᴇʟᴘʟɪɴᴇ Bᴏᴛ</a>\n├ <a href=https://t.me/EternalsHelplineBot>Hᴇʟᴘʟɪɴᴇ </a>\nTʜᴀɴᴋs Fᴏʀ ʏᴏᴜʀ Sᴜᴘᴘᴏʀᴛ</blockquote expandable></b>",
    "FSUB": "<b><blockquote>Hᴇʟʟᴏ!! {first} ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ <a href=https://t.me/Anime_Eternals>Aɴɪᴍᴇ Eᴛᴇʀɴᴀʟs</blockquote> </a> Yᴏᴜ ɴᴇᴇᴅ ᴛᴏ Jᴏɪɴ ɪɴ ᴍʏ Cʜᴀɴɴᴇʟ/Gʀᴏᴜᴘ ғɪʀsᴛ, Pʟᴇᴀsᴇ sᴜʙsᴄʀɪʙᴇ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴀɴᴅ sᴛᴀʀᴛ ʙᴏᴛ ᴀɢᴀɪɴ</a></b>",
    "ABOUT": "<b><blockquote>◈sᴜᴘʀᴇᴀᴍ : <a href='https://t.me/AnimeNexusNetwork'>ɴᴇᴛᴡᴏʀᴋ</a>\n◈ᴀɴɪᴍᴇ : <a href='https://t.me/Anime_Eternals'>ᴀɴɪᴍᴇ ᴇᴛᴇʀɴᴀʟꜱ</a>\n◈ᴏɴɢᴏɪɴɢ ᴀɴɪᴍᴇ: <a href='https://t.me/Anime_Ongoing_Airing'>ᴏɴɢᴏɪɴɢ ᴀɪʀɪɴɢꜱ</a>\n◈ᴇᴄᴄʜɪ : <a href='https://t.me/Ecchi_Dex'>ᴇᴄᴄʜɪ ᴅᴇx</a>\n◈ʜᴇʟᴘʟɪɴᴇ : <a href='https://t.me/EternalsHelplineBot'>ʜᴇʟᴘʟɪɴᴇ</a></b></blockquote>",
    "REPLY": "<b>For More Join - @Anime_Eternals</b>",
    "SHORT_MSG": "<b>📊 ʜᴇʏ {first}, \n\n‼️ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇꜱ ɪɴ ᴀ ꜱɪɴɢʟᴇ ʟɪɴᴋ ‼️\n\n ⌯ ʏᴏᴜʀ ʟɪɴᴋ ɪꜱ ʀᴇᴀᴅʏ, ᴋɪɴᴅʟʏ ᴄʟɪᴄᴋ ᴏɴ ᴏᴘᴇɴ ʟɪɴᴋ ʙᴜᴛᴛᴏɴ..</b>",
    "START_PHOTO": "https://graph.org/file/510affa3d4b6c911c12e3.jpg",
    "FSUB_PHOTO": "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg",
    "SHORT_PIC": "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg",
    "SHORT": "https://telegra.ph/file/8aaf4df8c138c6685dcee-05d3b183d4978ec347.jpg"
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
