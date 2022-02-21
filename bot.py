# © Cyril C Thomas
# https://t.me/cyril_c_10

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from pyrogram import Client, filters

logging.getLogger("pyrogram").setLevel(logging.WARNING)

from config import Config
from Spotify.downloader import downloader
from Spotify.broadcast import broadcast_handler
from Spotify.commands import status, start, helper
from Spotify.database.access_db  import db

cbot = Client(session_name=Config.SESSION_NAME,
              bot_token=Config.BOT_TOKEN,
              api_id=Config.API_ID,
              api_hash=Config.API_HASH)


@cbot.on_message(filters.command('start') & filters.private)
async def c_start(bot, update):
    await db.add_user(update.chat.id)
    await start(bot, update)

@cbot.on_message(filters.command('status') & filters.user(Config.BOT_OWNER))
async def c_status(_, update):
    await status(update)

@cbot.on_message(filters.private & filters.regex("spotify"))
async def c_files(bot, update):
    await db.add_user(update.chat.id)
    await downloader(bot, update)

@cbot.on_message(filters.command('help') & filters.private)
async def c_help(bot, update):
    await db.add_user(update.chat.id)
    await helper(bot, update)

@cbot.on_message(filters.command('broadcast') & filters.user(Config.BOT_OWNER))
async def c_status(_, update):
    await broadcast_handler(update)


cbot.run()