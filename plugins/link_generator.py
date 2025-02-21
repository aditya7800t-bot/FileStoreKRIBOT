from pyrogram import Client, filters from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton from bot import Bot from config import ADMINS from helper_func import encode, get_message_id import asyncio import time from database.join_reqs import JoinReqs

Database instance

jishubotz = JoinReqs()

Dictionary to store link expiry data

link_expiry = {}

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('generate_link')) async def generate_link(client: Client, message: Message): user_id = message.from_user.id link = f"https://t.me/{client.me.username}?start={int(time.time())}" link_expiry[user_id] = time.time() + 1800  # 30 minutes expiry

# Save in database
jishubotz.save_link(user_id, link, link_expiry[user_id])

await message.reply_text(f"Your link: {link}\n\nThis link will expire in 30 minutes and regenerate automatically.")

# Schedule deletion and regeneration
asyncio.create_task(auto_refresh_link(client, user_id))

async def auto_refresh_link(client: Client, user_id): await asyncio.sleep(1800)  # Wait for 30 minutes

if user_id in link_expiry and time.time() >= link_expiry[user_id]:
    new_link = f"https://t.me/{client.me.username}?start={int(time.time())}"
    link_expiry[user_id] = time.time() + 1800
    
    # Update database
    jishubotz.update_link(user_id, new_link, link_expiry[user_id])
    
    # Notify user
    try:
        await client.send_message(user_id, f"Your old link expired! Here is your new link: {new_link}")
    except Exception as e:
        print(f"Failed to notify user {user_id}: {e}")

