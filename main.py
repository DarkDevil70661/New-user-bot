# bot_manager.py
# ----------------------------------------------------
# Sirocco Dynamic Bot & Userbot Cloner System (Updated)
# ----------------------------------------------------

import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from telethon import TelegramClient
from telethon.sessions import StringSession

# ডায়নামিকালি চালু থাকা বটগুলোর তালিকা সংরক্ষণের জন্য ডিকশনারি
ACTIVE_BOTS = {}
ACTIVE_USERBOTS = {}

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    বট শুরু করার কমান্ড এবং নির্দেশিকা (প্লেন টেক্সট)।
    """
    help_text = (
        "🤖 Sirocco Bot & Userbot Cloner\n\n"
        "To clone a bot or run your Userbot along with the clone, please use the command below:\n\n"
        "👉 Clone & Run:\n"
        "/clone <STRING_SESSION>\n\n"
        "(Note: Provide your String Session along with the command to get your Userbot ready instantly!)"
    )
    await update.message.reply_text(help_text)


async def clone_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    সেশন দিয়ে ইউজারবট এবং ক্লোন বট রান করবে।
    """
    args = context.args
    if not args:
        await update.message.reply_text(
            "⚠️ Please provide your String Session!\n"
            "Usage: /clone <STRING_SESSION>"
        )
        return

    string_session = args[0]
    
    # আপনার মাস্টার বট টোকেন এখানে অটোমেটিক বট ক্লোন করার জন্য ব্যবহার করা যেতে পারে
    bot_token = "8795990981:AAFA57XvuHVjzBcaED1T-YLHsj5VgqeRR4k"

    if bot_token in ACTIVE_BOTS:
        await update.message.reply_text("⚠️ This bot token is already active!")
        return

    try:
        await update.message.reply_text("🔄 Processing... Setting up your cloned bot and userbot, please wait.")
        
        # ১. নতুন বট ক্লোন ও রান করা
        new_app = ApplicationBuilder().token(bot_token).build()
        
        async def dynamic_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
            if update.message and update.message.text:
                await update.message.reply_text(f"🤖 Automated Reply from Cloned Bot: {update.message.text}")

        new_app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), dynamic_reply))
        
        await new_app.initialize()
        await new_app.start()
        await new_app.updater.start_polling()
        ACTIVE_BOTS[bot_token] = new_app

        # ২. ইউজারবট রান করা (ডিফল্ট API_ID এবং API_HASH ব্যবহার করে অথবা সরাসরি স্ট্রিং সেশন দিয়ে)
        userbot_status = ""
        try:
            # টেলিগ্রামের ডিফল্ট পাবলিক API_ID এবং API_HASH অথবা আপনার নিজস্ব দিতে পারেন
            api_id = 31260540
            api_hash = "cd213befc727364a96df92d26852bd89"
            
            client = TelegramClient(StringSession(string_session), int(api_id), api_hash)
            await client.start()
            me = await client.get_me()
            ACTIVE_USERBOTS[me.id] = client
            userbot_status = f"\n\n👤 Userbot Ready: {me.first_name} ({me.id})"
        except Exception as ue:
            userbot_status = f"\n\n⚠️ Bot cloned successfully, but Userbot failed: {str(ue)}"

        await update.message.reply_text(
            f"✅ Success! Your cloned bot has been successfully deployed and started.{userbot_status}"
        )
        
    except Exception as e:
        await update.message.reply_text(f"❌ Failed to start bot: {str(e)}")


async def main_async():
    # মেইন কন্ট্রোল বট টোকেন
    MASTER_TOKEN = "8795990981:AAFA57XvuHVjzBcaED1T-YLHsj5VgqeRR4k"
    
    print("=" * 60)
    print("   Sirocco Master Bot Cloner & Session Runner Starting...")
    print("=" * 60)
    
    app = ApplicationBuilder().token(MASTER_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("clone", clone_bot))
    
    # অ্যাসিনক্রোনাস পদ্ধতিতে বট ইনিশিয়ালাইজ ও স্টার্ট করা
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
