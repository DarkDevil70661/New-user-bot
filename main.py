# bot_manager.py
# ----------------------------------------------------
# Sirocco Multi-Userbot Auto Runner System (10 Slots)
# ----------------------------------------------------

import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# সক্রিয় ইউজারবটগুলো সংরক্ষণের জন্য ডিকশনারি
ACTIVE_USERBOTS = {}

# এখানে মোট ১০টি সেশনের স্লট রাখা হয়েছে। 
# আপনি আপনার প্রয়োজন অনুযায়ী সেশন স্ট্রিংগুলো কোটেশনের ভেতরে বসাতে পারেন।
# যদি কোনো স্লট ফাঁকা রাখতে চান, তবে ফাঁকা স্ট্রিং "" অথবা None রাখতে পারেন।
USERBOT_SESSIONS = [
    # Slot 1 (আপনার দেওয়া বর্তমান সেশনটি এখানে বসানো আছে)
    "BQH9_DgAiv8xPGnqsDW9hYNKOLoaOtoY6mnW4-Mblnefr5QalaroXfVj32Yb9c02HZuO8Y9nAwenzTByI4TZmRKZ_NC3OHYFjt5yiOtBI7R_sfgdoXtv0o-6G8tidfnUO5p5urgECgASRxtnVlNd45iCHKiqRX2k_DfjsiSm70TA7VI9eindX4Y9huO7nhiDeQFQeVdbCiikDg3HoPnrufhY_u6Z_A96wMFB3HexZ58a6r5pR2NldKsq6QUZtXeAwEk-EbYb1ewG53HncFostUVZLxQF-jDjC9oy3_QMDSVwy5aS7QZurgTIO_k5gBANnXAAUpQaPW6YwJOBlci9_9vdspLeJAAAAAGWtFfFAA",
    
    # Slot 2 থেকে 10 (ফাঁকা রাখা হয়েছে, পরবর্তীতে প্রয়োজন অনুযায়ী সেশন বসাতে পারবেন)
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    ""
]

async def start_userbots():
    """
    কোডের লিস্টে থাকা প্রতিটি ভ্যালিড সেশন চেক করে ব্যাকগ্রাউন্ডে অটোমেটিক রান করবে।
    """
    api_id = 33422392  
    api_hash = "9b66ed5b9e6a307951b3a681c80f9d4b"
    
    print("=" * 60)
    print("   Sirocco Multi-Userbot Auto Runner Starting...")
    print("=" * 60)

    for index, session_str in enumerate(USERBOT_SESSIONS, start=1):
        cleaned_session = session_str.strip().replace("'", "").replace('"', "")
        
        # যদি স্লট ফাঁকা থাকে তবে স্কিপ করবে
        if not cleaned_session:
            print(f"[-] Userbot Slot {index}: Empty (Skipped)")
            continue
            
        try:
            print(f"[+] Connecting Userbot Slot {index}...")
            client = TelegramClient(StringSession(cleaned_session), int(api_id), api_hash)
            
            await asyncio.wait_for(client.connect(), timeout=20.0)
            
            if await client.is_user_authorized():
                me = await client.get_me()
                ACTIVE_USERBOTS[me.id] = client
                print(f"✅ Userbot Slot {index} Connected Successfully! -> {me.first_name} (`{me.id}`)")
            else:
                print(f"❌ Userbot Slot {index}: Session is unauthorized or expired!")
                await client.disconnect()
                
        except asyncio.TimeoutError:
            print(f"❌ Userbot Slot {index}: Connection timed out!")
        except Exception as e:
            print(f"❌ Userbot Slot {index} Error: {str(e)}")

    print("=" * 60)
    print("   All Userbot slots processed. Running continuously...")
    print("=" * 60)

    # বট এবং ইউজারবটগুলো সচল রাখার জন্য ইনফিনিট লুপ
    stop_event = asyncio.Event()
    await stop_event.wait()

def main():
    try:
        asyncio.run(start_userbots())
    except KeyboardInterrupt:
        print("\n[!] Userbots stopped by user.")

if __name__ == "__main__":
    main()
