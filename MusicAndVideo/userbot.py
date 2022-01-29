import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("Minggu", 60 * 60 * 24 * 7),
    ("Hari", 60 * 60 * 24),
    ("Jam", 60 * 60),
    ("Menit", 60),
    ("Detik", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["ping"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("⚡")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>🏓 PONG</b> `{delta_ping * 1000:.3f} ms` \n<b>⏳ ACTIVE</b> - `{uptime}`"
    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**✅ Userbot Restarted**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>👋 Hello {m.from_user.mention}!

🛠 MENU HELP

⚡ FOR EVERYONE
• {HNDLR}play [song Name | link youtube | reply file audio] - to play a song
• {HNDLR}vplay [Video Song Name | link youtube | reply file video] - to play videos
• {HNDLR}playlist to view playlist
• {HNDLR}ping - To check status
• {HNDLR}help - to see a list of commands

⚡ FOR SUDO AND ADMIN
• {HNDLR}resume - To continue playing a song or video
• {HNDLR}pause - To pause song or video
• {HNDLR}skip - To skip song or  video
• {HNDLR}end - To end song and userbot will leave the vc</b>
"""
    await m.reply(HELP)


@Client.on_message(filters.command(["repo"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>👋 Hello {m.from_user.mention}!

🎶 this is an  MusicAndVideo  Player bot made by @itzamanrajput

🤖 Telegram UserBot To Play Songs And Videos In Telegram Voice Chat.

✨ Presented by 
• [AMAN RAJPUT](https://t.me/itzamanrajput)
• [SUPPORT GROUP](https://t.me/himu_ki_jaan)


📝 Condition
• Python 3.8+
• FFMPEG
• Nodejs v16+

🛠 MENU HELP

⚡ ORDER FOR EVERYONE
• `/play [SONG NAME | link youtube | REPLY file audio]` - To play audio song
• `/vplay [Video song Name | link youtube | reply file video]` - To play video
• `/playlist` To view playlist
• `/ping` - To check status
• `/help` - To view commands

⚡ ORDER FOR ALL ADMIN
• `/resume` - To start playing song or video
• `/pause` - To Pause song or video
• `/skip` - To skip song or video
• `/end` - To end songs and userbot will leave the vc

💡 Deployment

💜 Heroku

 [𝗗𝗘𝗣𝗟𝗢𝗬 To𝗘 𝗛𝗘𝗥𝗢𝗞𝗨](https://heroku.com/deploy?template=https://github.com/amanrajput2001/musicuserbot2.0)

📚 Variable Required
• `API_ID` - Get From [my.telegram.org](https://my.telegram.org)
• `API_HASH` - Get From [my.telegram.org](https://my.telegram.org)
• `SESSION` - Create String Pyrogram. Create it From  [Sini](https://replit.com/@GoodBoysExe/string-session?lite=1&outputonly=1)
• `SUDO_USER` - ID Of Telegram Account Used As  Admin


🔥 CREDIT 
• No ANY CREDIT TO ANYONE</b>
"""
    await m.reply(REPO, disable_web_page_preview=True)

