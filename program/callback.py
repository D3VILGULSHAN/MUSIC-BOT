from driver.queues import QUEUE
from pyrogram import Client, filters
from program.utils.inline import menu_markup
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"""✨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) allows you to play music and video on groups through the new Telegram's video chats!**
💡 **Find out all the Bot's commands and how they work by clicking on the » 📚 Commands button!**
🔖 **To know how to use this bot, please click on the » ❓ Basic Guide button!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add me to your Group ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Basic Guide", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Commands", callback_data="cbcmds"),
                    InlineKeyboardButton("❤ Donate", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🌐 Source Code", url="https://github.com/PRAGULOFFICIAL/MUSIC-BOT/"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f"""❓ How to use this Bot ?, read the Guide below !
1.) First, add this bot to your Group.
2.) Then, promote this bot as administrator on the Group also give all permissions except Anonymous admin.
3.) After promoting this bot, type /reload in Group to update the admin data.
3.) Invite @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her (unfortunately the userbot will joined by itself when you type `/play (song name)` or `/vplay (song name)`).
4.) Turn on/Start the video chat first before start to play video/music.
`- END, EVERYTHING HAS BEEN SETUP -`
📌 If the userbot not joined to video chat, make sure if the video chat already turned on and the userbot in the chat.
💡 If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**
»  CHOOSE THE MENU BELOW TO READ THE EXPLANATION & SEE THE LIST OF AVAILABLE COMMANDS !
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷ADMIN CMNDS 👷‍♂", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙SUDO CMNDS 🧙", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("BASIC COMMANDS 📚", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""🏮 HERE IS THE BASIC COMMANDS:
» /play (SONG NAME/LINK) - PLAY MUSIC ON VIDEO CHAT
» /vplay (VIDEO NAME/LINK) - PLAY VIDEO ON VIDEO CHAT
» /vstream - PLAY LIVE VIDEO FROM YT LIVE/M3U8
» /playlist - SHOW YOU THE PLAYLIST
» /video (QUERY) - DOWNLOAD VIDEO FROM YOUTUBE
» /song (QUERY) - DOWNLOAD SONG FROM YOUTUBE
» /lyric (QUERY) - SCRAP THE SONG LYRIC
» /search (QUERY) - SEARCH A YOUTUBE VIDEO LINK
» /ping - SHOW THE BOT PING STATUS
» /uptime - SHOW THE BOT UPTIME STATUS
» /alive  - SHOW THE BOT ALIVE INFO (IN GROUP ONLY)
⚡️ __Powered by {BOT_NAME} """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("GO BACK 🔙", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""🏮 here is the admin commands:
» /pause - PAUSE THE STREAM
» /resume - RESUME THE STREAM
» /skip - SWITCH TO NEXT STREAM
» /stop - STOP THE STREAMING
» /vmute - MUTE THE USERBOT ON VOICE CHAT
» /vunmute - UNMUTE THE USERBOT ON VOICE CHAT
» /volume `1-200` - ADJUST THE VOLUME OF MUSIC (USERBOT MUST BE ADMIN)
» /reload - RELOAD BOT AND REFRESH THE ADMIN DATA
» /userbotjoin - INVITE THE USERBOT TO JOIN GROUP
» /userbotleave - ORDER USERBOT TO LEAVE FROM GROUP
⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.answer("sudo commands")
    await query.edit_message_text(
        f"""🏮 here is the sudo commands:
» /gban (`USERNAME` OR `USER ID`) - FOR GLOBAL BANNED PEOPLE
» /ungban (`USERNAME` OR `USER ID`) - FOR UN-GLOBAL BANNED PEOPLE
» /speedtest - RUN THE BOT SERVER SPEEDTEST
» /sysinfo - SHOW THE SYSTEM INFORMATION
» /update - UPDATE YOUR BOT TO LATEST VERSION
» /restart - RESTART YOUR BOT
» /leaveall - ORDER USERBOT TO LEAVE FROM ALL GROUP
» /leavebot (`CHAT ID`) - ORDER BOT TO LEAVE FROM THE GROUP YOU SPECIFY
» /eval - EXECUTE ANY CODE
» /sh - RUN ANY COMMAND
» /broadcast (`message`) -  SEND A BROADCAST MESSAGE TO ALL GROUPS ENTERED BY BOT
» /broadcast_pin (`message`) - SEND A BROADCAST MESSAGE TO ALL GROUPS ENTERED BY BOT WITH THE CHAT PIN
⚡ __Powered by {BOT_NAME} """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("GO BACK 🔙", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 ONLY ADMIN WITH MANAGE VIDEO CHAT PERMISSION THAT CAN TAP THIS BUTTON !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    chat = query.message.chat.title
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **SETTINGS OF** {CHAT}\N\N⏸ : PAUSE STREAM\N▶️ : RESUME STREAM\N🔇 : MUTE USERBOT\N🔊 : UNMUTE USERBOT\N⏹ : STOP STREAM",
              reply_markup=InlineKeyboardMarkup(buttons),
          )
    else:
        await query.answer("❌ NOTHING IS CURRENTLY STREAMING", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 ONLY ADMIN WITH MANAGE VIDEO CHAT PERMISSION THAT CAN TAP THIS BUTTON !", show_alert=True)
    await query.message.delete()
