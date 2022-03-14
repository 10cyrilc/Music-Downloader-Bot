# © Cyril C Thomas
# https://t.me/cyril_c_10

import aiofiles
import asyncio
import os

from config import Config


async def spot_downloader(bot, update):
    try:
        os.makedirs("./downloads/spot")
    except FileExistsError:
        pass

    reply_ = await update.reply("🔎")

    download_path = f"./downloads/spot/{update.chat.id}/"

    try:
        os.makedirs(download_path)
    except FileExistsError:
        pass

    song_ur = update.text.split("&")[0]
    song_url = f"spotdl {song_ur} -o {download_path}"
    # print(song_url)

    proc = await asyncio.create_subprocess_shell(
        song_url, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    # print(stdout)
    try:
        std_err = stderr.decode()
        std_out = stdout.decode()
    except UnicodeDecodeError:
        std_err
    # print(std_err)
    # print(std_out)

    if std_err:
        try:
            if os.path.isdir(download_path):
                directory_contents = os.listdir(download_path)
                directory_contents.sort()
                for files in directory_contents:
                    if "cache" not in files:
                        await reply_.edit("💥")
                        await spot_upload(bot, update, files)
                        await reply_.edit("⚡️")
        except Exception as e:
            print(e)
            await reply_.edit("Song not Found......!!!!\n\nContact @c_bots_support")
    else:
        if os.path.isdir(download_path):
            directory_contents = os.listdir(download_path)
            directory_contents.sort()
            for files in directory_contents:
                if "cache" not in files:
                    await reply_.edit("💥")
                    await spot_upload(bot, update, files)
                    await reply_.edit("⚡️")
    await reply_.delete()


async def yt_downloader(bot, update):
    try:
        os.makedirs("./downloads/yt")
    except FileExistsError:
        pass

    reply_ = await update.reply("🔎")

    download_path = f"./downloads/yt/{update.chat.id}/"

    try:
        os.makedirs(download_path)
    except FileExistsError:
        pass

    song_url = f"yt-dlp -x {update.text} --add-metadata --embed-thumbnail  --audio-format mp3 --metadata-from-title='%(artist)s - %(title)s' --prefer-ffmpeg -o {download_path}'%(title)s.%(ext)s'"

    proc = await asyncio.create_subprocess_shell(
        song_url, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    # print(stdout)
    # print("------------------------------------------------------------------------------")
    # print(stderr)
    std_err = stderr.decode()
    std_out = stdout.decode()
    try:
        if os.path.isdir(download_path):
            directory_contents = os.listdir(download_path)
            directory_contents.sort()
            for files in directory_contents:
                await reply_.edit("💥")
                await yt_uploader(bot, update, files)
                await reply_.edit("⚡️")
            await reply_.delete()
    except Exception as e:
        print(e)
        await reply_.edit("Song not Found......!!!!\n\nContact @c_bots_support")


async def spot_upload(bot, update, file_name):
    download_path = f"./downloads/spot/{update.chat.id}/{file_name}"
    thum_ = "./Song/thumb.jpg"
    song_me = await bot.send_audio(
        chat_id=update.chat.id,
        audio=download_path,
        thumb=thum_,
        reply_to_message_id=update.message_id
    )
    for_ = await song_me.forward(chat_id=Config.LOG_CHANNEL)
    await bot.send_message(text=f"**User:** [{update.from_user.first_name}](tg://user?id={str(update.from_user.id)})\n**Username:** `{update.from_user.username}`\n**UserID:** `{update.from_user.id}`",
                           disable_web_page_preview=True,
                           chat_id=Config.LOG_CHANNEL,
                           reply_to_message_id=for_.message_id
                           )
    await aiofiles.os.remove(download_path)


async def yt_uploader(bot, update, file_name):
    download_path = f"./downloads/yt/{update.chat.id}/{file_name}"
    thum_ = "./Song/thumb.jpg"
    song_me = await bot.send_audio(
        chat_id=update.chat.id,
        audio=download_path,
        thumb=thum_,
        reply_to_message_id=update.message_id
    )
    for_ = await song_me.forward(chat_id=Config.LOG_CHANNEL)
    await bot.send_message(text=f"**User:** [{update.from_user.first_name}](tg://user?id={str(update.from_user.id)})\n**Username:** `{update.from_user.username}`\n**UserID:** `{update.from_user.id}`",
                           disable_web_page_preview=True,
                           chat_id=Config.LOG_CHANNEL,
                           reply_to_message_id=for_.message_id
                           )
    await aiofiles.os.remove(download_path)
