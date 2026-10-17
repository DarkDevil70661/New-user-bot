# bot_manager.py
# ----------------------------------------------------
# Sirocco Dynamic Bot & Userbot Cloner System
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
    বট শুরু করার কমান্ড এবং নির্দেশিকা (সম্পূর্ণ ইংরেজিতে)।
    """
    help_text = (
        "🤖 **Sirocco Bot & Userbot Cloner**\n\n"
        "To clone a bot or run your Userbot along with the clone, please use the command below:\n\n"
        "👉 **Clone & Run:**\n"
        "`/clone <BOT_TOKEN> <API_ID> <API_HASH> <STRING_SESSION>`\n\n"
        "*(Note: Provide your API ID, API Hash, and String Session along with the Bot Token to get your Userbot ready instantly!)*"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")


async def clone_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    টোকেন দিয়ে বট ক্লোন করবে এবং সেশন দেওয়া থাকলে ইউজারবটও একসাথে রান করবে।
    """
    args = context.args
    if not args:
        await update.message.reply_text(
            "⚠️ Please provide your Bot Token and session details!\n"
            "Usage: `/clone <BOT_TOKEN> <API_ID> <API_HASH> <STRING_SESSION>`",
            parse_mode="Markdown"
        )
        return

    bot_token = args[0]
    
    # চেক করা হচ্ছে সাথে ইউজারবটের সেশন দেওয়া হয়েছে কি না
    has_session = len(args) >= 4
    api_id = args[1] if has_session else None
    api_hash = args[2] if has_session else None
    string_session = args[3] if has_session else None

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
        asyncio.create_task(new_app.updater.start_polling())
        ACTIVE_BOTS[bot_token] = new_app

        # ২. যদি সেশন দেওয়া থাকে, তবে ইউজারবটও রান করা
        userbot_status = ""
        if has_session:
            try:
                client = TelegramClient(StringSession(string_session), int(api_id), api_hash)
                await client.start()
                me = await client.get_me()
                ACTIVE_USERBOTS[me.id] = client
                userbot_status = f"\n\n👤 **Userbot Ready:** {me.first_name} (`{me.id}`)"
            except Exception as ue:
                userbot_status = f"\n\n⚠️ Bot cloned successfully, but Userbot failed: `{str(ue)}`"

        await update.message.reply_text(
            f"✅ Success! Your cloned bot has been successfully deployed and started.{userbot_status}",
            parse_mode="Markdown"
        )
        
    except Exception as e:
        await update.message.reply_text(f"❌ Failed to start bot: `{str(e)}`", parse_mode="Markdown")


def main():
    # মেইন কন্ট্রোল বট টোকেন
    MASTER_TOKEN = "8795990981:AAFA57XvuHVjzBcaED1T-YLHsj5VgqeRR4k"
    
    print("=" * 60)
    print("   Sirocco Master Bot Cloner & Session Runner Starting...")
    print("=" * 60)
    
    app = ApplicationBuilder().token(MASTER_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("clone", clone_bot))
    
    print("Master Bot is running... Send /start in Telegram.")
    app.run_polling()

if __name__ == "__main__":
    main()
