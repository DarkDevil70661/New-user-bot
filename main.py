# bot_manager.py
# ----------------------------------------------------
# Sirocco Userbot Runner System (Interactive Session Input)
# ----------------------------------------------------

import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from telethon import TelegramClient
from telethon.sessions import StringSession

# সক্রিয় ইউজারবটগুলো সংরক্ষণের জন্য ডিকশনারি
ACTIVE_USERBOTS = {}
# ইউজারের স্টেট ট্র্যাক করার জন্য (কার জন্য সেশন চাওয়া হচ্ছে)
WAITING_FOR_SESSION = set()

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    বট শুরু করার কমান্ড এবং নির্দেশিকা।
    """
    help_text = (
        "🤖 Sirocco Userbot Runner\n\n"
        "To run your Userbot, simply use the command below:\n\n"
        "👉 `/clone`\n\n"
        "(The bot will ask for your String Session safely without any argument cut-off issues!)"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")


async def clone_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    ইউজারকে সেশন পাঠানোর জন্য প্রম্পট করবে।
    """
    user_id = update.effective_user.id
    WAITING_FOR_SESSION.add(user_id)
    await update.message.reply_text(
        "📥 Please send your Telegram String Session now as a plain text message:"
    )


async def handle_session_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    ইউজারের পাঠানো সেশন রিসিভ করে ইউজারবট রান করবে।
    """
    user_id = update.effective_user.id
    if user_id not in WAITING_FOR_SESSION:
        return

    # স্টেট রিমুভ করা
    WAITING_FOR_SESSION.remove(user_id)
    
    # সেশন টেক্সট ক্লিন করা (কোনো অতিরিক্ত স্পেস বা কোটেশন থাকলে রিমুভ)
    string_session = update.message.text.strip().replace("'", "").replace('"', "")

    status_msg = await update.message.reply_text("🔄 Processing... Connecting your Userbot to Telegram, please wait...")

    try:
        api_id = 33422392  
        api_hash = "9b66ed5b9e6a307951b3a681c80f9d4b"
        
        # Telethon ক্লায়েন্ট তৈরি
        client = TelegramClient(StringSession(string_session), int(api_id), api_hash)
        
        # কানেক্ট করার চেষ্টা এবং ৩০ সেকেন্ডের টাইমআউট
        await asyncio.wait_for(client.connect(), timeout=30.0)
        
        if not await client.is_user_authorized():
            await status_msg.edit_text("❌ Failed to start Userbot: The provided String Session is unauthorized or expired!")
            await client.disconnect()
            return
            
        me = await client.get_me()
        
        if me.id in ACTIVE_USERBOTS:
            await status_msg.edit_text("⚠️ This Userbot session is already active!")
            await client.disconnect()
            return
            
        ACTIVE_USERBOTS[me.id] = client
        
        await status_msg.edit_text(
            f"✅ Success! Your Userbot has been successfully connected and started.\n\n"
            f"👤 User: {me.first_name} (`{me.id}`)",
            parse_mode="Markdown"
        )
        
    except asyncio.TimeoutError:
        await status_msg.edit_text("❌ Connection timed out! Telegram servers took too long to respond. Please try again.")
    except Exception as e:
        await status_msg.edit_text(f"❌ Failed to start Userbot: `{str(e)}`", parse_mode="Markdown")


async def main_async():
    MASTER_TOKEN = "8795990981:AAFA57XvuHVjzBcaED1T-YLHsj5VgqeRR4k"
    
    print("=" * 60)
    print("   Sirocco Master Bot & Userbot Runner Starting...")
    print("=" * 60)
    
    app = ApplicationBuilder().token(MASTER_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("clone", clone_command))
    # যেকোনো সাধারণ টেক্সট মেসেজ হ্যান্ডেল করার জন্য (যখন সেশন পাঠাবে)
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_session_message))
    
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    
    print("Master Bot is running successfully...")
    
    stop_event = asyncio.Event()
    await stop_event.wait()


def main():
    try:
        asyncio.run(main_async())
    except KeyboardInterrupt:
        print("Bot stopped by user.")

if __name__ == "__main__":
    main()
