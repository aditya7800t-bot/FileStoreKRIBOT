from pyrogram import Client,filters,enums
from pyrogram.types import ChatJoinRequest
InlineKeyboardMarkup, InlineKeyboardButton
from database.join_reqs import JoinReqs
from config import ADMINS, FORCE_SUB_CHANNEL
import asyncio
import time


jishubotz = JoinReqs

Dictionary to store link expiry data

link_expiry = {}

@Client.on_chat_join_request(filters.chat(FORCE_SUB_CHANNEL if FORCE_SUB_CHANNEL else "self")) async def join_reqs(client, join_req: ChatJoinRequest): if jishubotz().isActive(): user_id = join_req.from_user.id first_name = join_req.from_user.first_name username = join_req.from_user.username date = join_req.date

join_link = f"https://t.me/{FORCE_SUB_CHANNEL}"  # Force Subscribe Link
    link_expiry[user_id] = time.time() + 1800  # 30 minutes expiry
    
    await jishubotz().add_user(
        user_id=user_id,
        first_name=first_name,
        username=username,
        date=date
    )
    
    await join_req.approve()
    await client.send_message(
        user_id,
        f"Hello {first_name},\nYou need to join our channel to use the bot.\n\n**Join Here:** {join_link}\n(This link will expire in 30 minutes.)",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("JOIN CHANNEL", url=join_link)]]
        )
    )
    
    # Schedule link refresh
    asyncio.create_task(refresh_join_link(client, user_id))

async def refresh_join_link(client: Client, user_id): await asyncio.sleep(1800)  # Wait for 30 minutes

if user_id in link_expiry and time.time() >= link_expiry[user_id]:
    new_link = f"https://t.me/{FORCE_SUB_CHANNEL}?start={int(time.time())}"
    link_expiry[user_id] = time.time() + 1800
    
    # Notify user with new link
    try:
        await client.send_message(
            user_id,
            f"Your old join link expired! Here is your new link: {new_link}",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("JOIN CHANNEL", url=new_link)]]
            )
        )
    except Exception as e:
        print(f"Failed to notify user {user_id}: {e}")

