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

 [𝗗𝗘𝗣𝗟𝗢𝗬 To𝗘 𝗛𝗘𝗥𝗢𝗞𝗨](data:image/jpeg;base64,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)

📚 Variable Required
• `API_ID` - Get From [my.telegram.org](https://my.telegram.org)
• `API_HASH` - Get From [my.telegram.org](https://my.telegram.org)
• `SESSION` - Create String Pyrogram. Create it From  [Sini](https://replit.com/@GoodBoysExe/string-session?lite=1&outputonly=1)
• `SUDO_USER` - ID Of Telegram Account Used As  Admin


🔥 CREDIT 
• @fUckEd_uP_bY_LiFE BROTHER ❤️
@A_B_HA_Y ODU BRO❤️ </b>
"""
    await m.reply(REPO, disable_web_page_preview=True)

