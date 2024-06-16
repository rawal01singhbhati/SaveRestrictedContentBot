#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=16494736, cast=int)
API_HASH = config("API_HASH", default=2cb7fa5859e2de684e3e10d9c049621a)
BOT_TOKEN = config("BOT_TOKEN", default=7394117438:AAH9ZtfA1ufzgOFELtpF81xRJGOFJOZtNEo)
SESSION = config("SESSION", default=BQD7sJAACl1e1g8UbOfrBvsx4T2rZETGwb8MKNibESFDWlKnv-4BGhXOthjIozwiSxrBy1RyWm4hfEEiHMjraX-r8gMtV_0hWmxqlcJx6AQlF5Odis4ZFVD_8bEohJZGk9XJAD64Pchz9zCY5ebWqV0yod6eDpAyRJsdCCmaeSrctK9rnK1YkYHb_VXznVo11I8BB4-Dopg1C2vYvsUJYUwXiVpYGtQhetKxaB2R_J21sRx45N-owEairZPPsPcWPYoRCXIeQPYQrrJpPZmnFbIteRVxJaZVRHJchs2IMUo_2ii_1CKNYIMYFuL2bScxho7een2HREWRHY4ZmcD5sMZB88mTtQAAAAFyZkhvAA)
FORCESUB = config("FORCESUB", default=trail01trailsave)
AUTH = config("AUTH", default=6214273135, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
