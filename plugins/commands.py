import asyncio
import os
from datetime import datetime, timedelta

from pyrogram import Client, filters, emoji
from pyrogram.types import Message

from config import HNDLR, bot, call_py

USERBOT_HELP = f"""{emoji.LABEL}  **Common Commands**:
__available to group members of current voice chat__
__starts with / (slash) or ! (exclamation mark)__
\u2022 **{HNDLR}play**  reply with an audio to play/queue it
\u2022 **{HNDLR}vplay**  reply with an video to play/queue it
\u2022 **{HNDLR}playlist** show a playlist
\u2022 **{HNDLR}repo**  show git repository of the userbot
\u2002 **{HNDLR}playfrom** play from another group/channel
\u2022 `{HNDLR}help`  show help for commands

{emoji.LABEL}  **Admin Commands**:
__available to userbot account itself and its contacts__
__starts with {HNDLR}
\u2022 `{HNDLR}skip` [n] ...  skip current or n where n >= 2
\u2022 `{HNDLR}stop`  stop playing
\u2022 `{HNDLR}pause` pause playing
\u2022 `{HNDLR}resume` resume playing
"""

USERBOT_REPO = f"""{emoji.ROBOT} **Telegram Voice Chat UserBot**
- Repository: [GitHub](https://github.com/lushaimusic/vc-userbot)
- License: GPL-3.0-or-later"""

@Client.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
async def show_help(_, m: Message):
    if mp.msg.get('help') is not None:
        await mp.msg['help'].delete()
    mp.msg['help'] = await m.reply_text(USERBOT_HELP, quote=False)
    await m.delete()

@Client.on_message(filters.command(["repo"], prefixes=f"{HNDLR}"))
async def show_repository(_, m: Message):
    if mp.msg.get('repo') is not None:
        await mp.msg['repo'].delete()
    mp.msg['repo'] = await m.reply_text(
        USERBOT_REPO,
        disable_web_page_preview=True,
        quote=False
    )
    await m.delete()
