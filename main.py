# bot_manager.py
# ----------------------------------------------------
# Sirocco Userbot Runner System (String Cleaner Fixed)
# ----------------------------------------------------

import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telethon import TelegramClient
from telethon.sessions import StringSession

# সক্রিয় ইউজারবটগুলো সংরক্ষণের জন্য ডিকশনারি
ACTIVE_USERBOTS = {}

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    বট শুরু করার কমান্ড এবং নির্দেশিকা (প্লেন টেক্সট)।
    """
    help_text = (
        "🤖 Sirocco Userbot Runner\n\n"
        "To run your Userbot, please use the command below:\n\n"
        "👉 Run Userbot:\n"
        "/clone <STRING_SESSION>\n\n"
        "(Note: Provide your Telegram String Session with the command to start your Userbot instantly!)"
    )
    await update.message.reply_text(help_text)


async def clone_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    স্ট্রিং সেশন ক্লিন করে ইউজারবট রান করবে।
    """
    args = context.args
    if not args:
        await update.message.reply_text(
            "⚠️ Please provide your String Session!\n"
            "Usage: /clone <STRING_SESSION>"
        )
        return

    # ব্যবহারকারীর দেওয়া সেশন থেকে অতিরিক্ত স্পেস, এন্টার বা কোটেশন রিমুভ করা
    string_session = " ".join(args).strip().replace("'", "").replace('"', "")

    try:
        await update.message.reply_text("🔄 Processing... Cleaning session and connecting your Userbot, please wait.")
        
        # টেলিগ্রামের ডিফল্ট API_ID এবং API_HASH
        api_id = 33422392
        api_hash = "9b66ed5b9e6a307951b3a681c80f9d4b"
        
        # Telethon ব্যবহার করে ইউজারবট ক্লায়েন্ট চালু করা
        client = TelegramClient(StringSession(string_session), int(api_id), api_hash)
        await client.start()
        
        me = await client.get_me()
        if me.id in ACTIVE_USERBOTS:
            await update.message.reply_text("⚠️ This Userbot session is already active!")
            return
            
        ACTIVE_USERBOTS[me.id] = client
        
        await update.message.reply_text(
            f"✅ Success! Your Userbot has been successfully connected and started.\n\n"
            f"👤 User: {me.first_name} ({me.id})"
        )
        
    except Exception as e:
        await update.message.reply_text(f"❌ Failed to start Userbot: {str(e)}")


async def main_async():
    # মেইন কন্ট্রোল বট টোকেন
    MASTER_TOKEN = "8795990981:AAFA57XvuHVjzBcaED1T-YLHsj5VgqeRR4k"
    
    print("=" * 60)
    print("   Sirocco Master Bot & Userbot Runner Starting...")
    print("=" * 60)
    
    app = ApplicationBuilder().token(MASTER_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("clone", clone_bot))
    
    # অ্যাসিনক্রোনাস পদ্ধতিতে মাস্টার বট ইনিশিয়ালাইজ ও স্টার্ট করা
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    
    print("Master Bot is running successfully...")
    
    # বট চালু রাখার জন্য ইনফিনিট লুপ
    stop_event = asyncio.Event()
    await stop_event.wait()


def main():
    try:
        asyncio.run(main_async())
    except KeyboardInterrupt:
        print("Bot stopped by user.")

if __name__ == "__main__":
    main()
