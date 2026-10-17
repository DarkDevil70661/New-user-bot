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
    বট শুরু করার কমান্ড এবং নির্দেশিকা।
    """
    help_text = (
        "🤖 **Sirocco Bot Cloner & Userbot Runner**\n\n"
        "নতুন বট বা ইউজারবট চালু করতে নিচের কমান্ডগুলো ব্যবহার করুন:\n"
        "1️⃣ **Bot Clone:** `/clone <BOT_TOKEN>`\n"
        "2️⃣ **Userbot Run:** `/runsession <API_ID> <API_HASH> <STRING_SESSION>`"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")


async def clone_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    ব্যবহারকারীর দেওয়া টেলিগ্রাম টোকেন দিয়ে তাৎক্ষণিকভাবে নতুন বট চালু করবে।
    """
    args = context.args
    if not args:
        await update.message.reply_text("⚠️ দয়া করে একটি সঠিক বট টোকেন দিন!\nব্যবহার: `/clone <BOT_TOKEN>`", parse_mode="Markdown")
        return

    bot_token = args[0]
    user_id = update.effective_user.id

    if bot_token in ACTIVE_BOTS:
        await update.message.reply_text("⚠️ এই টোকেনের বটটি ইতিমধ্যে চালু রয়েছে!")
        return

    try:
        await update.message.reply_text("🔄 নতুন বট তৈরি এবং চালু করা হচ্ছে, দয়া করে অপেক্ষা করুন...")
        
        # নতুন টেলিগ্রাম অ্যাপ্লিকেশন তৈরি করা
        new_app = ApplicationBuilder().token(bot_token).build()
        
        # নতুন বটের জন্য সাধারণ হ্যান্ডলার যোগ করা
        async def dynamic_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
            if update.message and update.message.text:
                await update.message.reply_text(f"🤖 হ্যালো! এটি ক্লোন করা বটের স্বয়ংক্রিয় উত্তর: {update.message.text}")

        new_app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), dynamic_reply))
        
        # ব্যাকগ্রাউন্ডে বট ইনিশিয়ালাইজ এবং রান করা
        await new_app.initialize()
        await new_app.start()
        # বট পোলিং শুরু করার জন্য ব্যাকগ্রাউন্ড টাস্ক
        asyncio.create_task(new_app.updater.start_polling())
        
        ACTIVE_BOTS[bot_token] = new_app
        await update.message.reply_text("✅ সফল! আপনার দেওয়া টোকেন দিয়ে নতুন বটটি সফলভাবে চালু এবং রান করা হয়েছে। 🎉")
        
    except Exception as e:
        # এখানে আগের ডট (.) ত্রুটি সংশোধন করা হয়েছে
        await update.message.reply_text(f"❌ বট চালু করতে সমস্যা হয়েছে: `{str(e)}`", parse_mode="Markdown")


async def run_userbot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    ব্যবহারকারীর টেলিগ্রাম স্ট্রিং সেশন (String Session) দিয়ে ইউজারবট রান করবে।
    """
    args = context.args
    if len(args) < 3:
        await update.message.reply_text(
            "⚠️ ভুল ফরম্যাট! সঠিক নিয়মে দিন:\n"
            "`/runsession <API_ID> <API_HASH> <STRING_SESSION>`",
            parse_mode="Markdown"
        )
        return

    api_id = args[0]
    api_hash = args[1]
    string_session = args[2]

    try:
        await update.message.reply_text("🔄 টেলিগ্রাম সেশন দিয়ে ইউজারবট কানেক্ট করা হচ্ছে...")
        
        # Telethon ব্যবহার করে ইউজারবট ক্লায়েন্ট তৈরি
        client = TelegramClient(StringSession(string_session), int(api_id), api_hash)
        await client.start()
        
        me = await client.get_me()
        ACTIVE_USERBOTS[me.id] = client
        
        await update.message.reply_text(
            f"✅ ইউজারবট সফলভাবে রান হয়েছে!\n"
            f"👤 **অ্যাকাউন্ট নাম:** {me.first_name}\n"
            f"🆔 **ইউজার আইডি:** `{me.id}`",
            parse_mode="Markdown"
        )
    except Exception as e:
        await update.message.reply_text(f"❌ ইউজারবট কানেক্ট করতে ব্যর্থ: `{str(e)}`", parse_mode="Markdown")


def main():
    # মেইন কন্ট্রোল বট টোকেন
    MASTER_TOKEN = "8795990981:AAFA57XvuHVjzBcaED1T-YLHsj5VgqeRR4k"
    
    print("=" * 60)
    print("   Sirocco Master Bot Cloner & Userbot Runner Starting...")
    print("=" * 60)
    
    app = ApplicationBuilder().token(MASTER_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("clone", clone_bot))
    app.add_handler(CommandHandler("runsession", run_userbot))
    
    print("Master Bot is running... Send /start in Telegram.")
    app.run_polling()

if __name__ == "__main__":
    main()
