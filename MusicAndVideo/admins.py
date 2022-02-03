from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, call_py
from MusicAndVideo.helpers.decorators import authorized_users_only
from MusicAndVideo.helpers.handlers import skip_current_song, skip_item
from MusicAndVideo.helpers.queues import QUEUE, clear_queue


@Client.on_message(filters.command(["skip"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def skip(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("**❌ 𝗯𝗰 𝗸𝘆𝗮 𝘀𝗸𝗶𝗽 𝗸𝗿𝘂? 𝗝𝗮𝗯 𝗾𝘂𝗲𝘂𝗲 𝗹𝗶𝘀𝘁 𝗺𝗲𝗶𝗻 𝗸𝗼𝗶 𝘀𝗼𝗻𝗴 𝗵𝗶 𝗻𝗮𝗵𝗶 𝗵𝗮𝗶🇮🇳**")
        elif op == 1:
            await m.reply("𝗤𝘂𝗲𝘂𝗲 𝗶𝘀 𝗲𝗺𝗽𝘁𝘆 𝗹𝗲𝗮𝘃𝗶𝗻𝗴 𝘃𝗼𝗶𝗰𝗲❤️🇮🇳**")
        else:
            await m.reply(
                f"**⏭ 𝗦𝗞𝗜𝗣 𝗛𝗢 𝗚𝗬𝗔❤️🇮🇳** \n**🎧 𝗔𝗕 𝗬𝗘 𝗖𝗛𝗔𝗟 𝗥𝗛𝗔 𝗛𝗔𝗜❤️🇮🇳** - [{op[0]}]({op[1]}) | `{op[2]}`",
                disable_web_page_preview=True,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "**🗑️ 𝗥𝗲𝗺𝗼𝘃𝗲𝗱 𝘁𝗵𝗲 𝗳𝗼𝗹𝗹𝗼𝘄𝗶𝗻𝗴 𝘀𝗼𝗻𝗴𝘀 𝗳𝗿𝗼𝗺 𝘁𝗵𝗲 𝗾𝘂𝗲𝘂𝗲❤️🇮🇳: -**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#⃣{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(filters.command(["end", "stop"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def stop(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("**✅ 𝗘𝗡𝗗𝗜𝗡𝗚 𝗣𝗟𝗔𝗬𝗕𝗔𝗖𝗞❤️🇮🇳**")
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply("**❌ 𝗸𝘂𝗰𝗵 𝗻𝗵𝗶 𝗰𝗵𝗮𝗹 𝗿𝗵𝗮 🙁!**")


@Client.on_message(filters.command(["pause"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def pause(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                f"**⏸ 𝗣𝗹𝗮𝘆 𝗯𝗮𝗰𝗸 𝗶𝘀 𝗽𝗮𝘂𝘀𝗲𝗱 𝗺𝗶𝘁 𝗴𝘆𝗶 𝗸𝗵𝘂𝗷𝗹𝗶?😆.**\n\n• 𝗿𝗲𝘀𝘂𝗺𝗲 𝗸𝗮𝗿𝗻𝗲 𝗸𝗲 𝗹𝗶𝘆𝗲 𝘆𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝘂𝘀𝗲 𝗸𝗿𝗻𝗮❤️🇮🇳 » {HNDLR}resume"
            )
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply("** ❌ 𝗸𝘂𝗰𝗵 𝗻𝗵𝗶 𝗰𝗵𝗮𝗹 𝗿𝗵𝗮 😡!**")


@Client.on_message(filters.command(["resume"], prefixes=f"{HNDLR}"))
@authorized_users_only
async def resume(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                f"**▶ 𝗿𝗲𝘀𝘂𝗺𝗲 𝗵𝗼 𝗴𝘆𝗮 𝗮𝗯 𝗺𝗮𝗷𝗲 𝗸𝗿❤️🇮🇳**\n\n• 𝗔𝗴𝗿 𝗳𝗶𝗿𝘀𝗲 𝗽𝗮𝘂𝘀𝗲 𝗸𝗿𝗻𝗲 𝗸𝗶 𝗰𝗵𝘂𝗹𝗹 𝗺𝗮𝗰𝗵𝗶 𝗵𝗮𝗶 𝘁𝗼 𝘆𝗲 𝘆𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝘂𝘀𝗲 𝗸𝗿😆 » {HNDLR}pause**"
            )
        except Exception as e:
            await m.reply(f"**ERROR** \n`{e}`")
    else:
        await m.reply("**❌ 𝗞𝘂𝗰𝗵 𝗻𝗮𝗵𝗶 𝗰𝗵𝗮𝗹 𝗿𝗮𝗵𝗮 𝘃𝗰 𝗽𝗲❤️🇮🇳!**")
