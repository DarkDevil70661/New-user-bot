# plugins/banglish_plugin.py
# ----------------------------------------------------
# Sirocco Bot - Banglish Plugin Module (Exact 100 Responses)
# ----------------------------------------------------

BANGLISH_RESPONSES = {
    # 1 - 10: Greetings & Small Talk
    "hello": "👋 Hello! Aj ami apnake kivabe sahajjo korte pari?",
    "hi": "✨ Hi there! Apnar jonno ki korte pari?",
    "kemon acho": "🤖 Ami bhalo achi, apnar kotha jiggesh korar jonno dhonnobad!",
    "tomar nam ki": "🤖 Amar nam Sirocco, apnar virtual assistant.",
    "khe baniyeche": "💻 Amake toyri kora hoyeche automatic reply dewar jonno.",
    "shuvo sokal": "🌅 Shuvo sokal! Apnar din-ti chomotkar katuk.",
    "shuvo dupur": "☀️ Shuvo dupur! Apnar din-ti kemon katche?",
    "shuvo sondha": "🌆 Shuvo sondha! Aj rate apnake kivabe sahajjo korte pari?",
    "nischoy bhalo": "🤝 Amaro khub bhalo laglo!",
    "tumi ki robot": "🤖 Ha, ami ekti automatic AI assistant.",

    # 11 - 20: Gratitude & Farewells
    "dhonnobad": "🙏 Apnake onek dhonnobad!",
    "thanks": "👍 Je kono somoy! Sahajjo korte pere anondito.",
    "onek dhonnobad": "💖 Apnar jonno shobshomoy sahajjo korte prostut.",
    "bye": "👋 Biday! Apnar din-ti darun katuk.",
    "shuvo ratri": "🌙 Shuvo ratri! Bhabe bishram nin.",
    "pore dekha hobe": "👀 Pore dekha hobe, bhalo thakben!",
    "bhalo din": "🌟 Dhonnobad! Apnar din-tio bhalo katuk.",
    "biday": "🕊️ Biday! Apnar shorbangin mongol kamona kori.",
    "bhalo theko": "🛡️ Apnio nirapode o bhalo thakben.",
    "tata": "👋 Tata! Abar kotha hobe.",

    # 21 - 30: Services & General Support
    "sahajjo": "🛠️ Apnar kon nirdishto bishoye sahajjo proyojon?",
    "support": "☎️ Amader support team 24 ghonta prostut ache.",
    "jogajog": "📧 Apni email ba live chat-er माध्यमe jogajog korte paren.",
    "seba": "⚡ Amra automatic messaging o processing seba diye thaki.",
    "somoy": "⏰ Amader seba shoptahar 7 din 24 ghontai chalu thake.",
    "location": "🌍 Amra online-e bishwa-byapi seba prodan kori.",
    "dam": "💲 Apnar pochhonder plan onujayi muljo nirdharito hoy.",
    "website": "🌐 Bistarito jante amader portal-e visit korun.",
    "feedback": "⭐ Apnar mulyoban feedback amader khubi proyojon.",
    "amader somporke": "📖 Amra sohoj jogajoger jonno smart chat solution dei.",

    # 31 - 40: Status & Orders
    "order status": "📦 Bortoman obostha jante apnar order ID prodan korun.",
    "track order": "🔍 Apnar tracking reference number-ti ekhane din.",
    "order batil": "❌ Shipment-er agei batil korar onurodh pathan.",
    "refund": "💸 Jachai-koron-er por 5 theke 7 karjobodibor modhye refund hoy.",
    "payment": "💳 Amra card, paypal ebong bank transfer grohon kori.",
    "discount": "🏷️ Amader home page-e bortoman offer-gulo dekhe nin.",
    "account": "👤 Apnar dashboard theke profile manage korte paren.",
    "password reset": "🔑 Login page-e 'Forgot Password' e click korun.",
    "registration": "📝 Apnar email diye khub sohoje registration korun.",
    "subscription": "🔔 Apnar subscription-er tottho settings option-e paben.",

    # 41 - 50: Clarifications & Fallbacks
    "tumi ki korte paro": "💡 Ami proshner uttor dite o tottho process korte pari.",
    "tumi ki ashol": "🤖 Ami ekti automatic AI assistant hisebe kaj korchi.",
    "manuser sathe kotha bolbo": "👤 Apnake ekjon support agent-er sathe jukto kora hocche.",
    "bhul uttor": "⚠️ Bhul bujhajujhir jonno dukkhito! Doya kore abar bolben?",
    "tottho chai": "📚 Apnar thik ki dhoroner tottho proyojon ta ullekh korun.",
    "eta ki free": "🎁 Moulik feature-gulo sompurno binamulyeye babohar korte paren.",
    "system update": "🔄 Amader system bortomaney latest version-e cholche.",
    "error": "🐞 Kono shomossha hole screenshot share korun.",
    "byasto": "⚡ Bortomaney amader server-e onek traffic royeche.",
    "default": "💬 Apnar bortar jonno dhonnobad! Ar kibabe sahajjo korte pari?",

    # 51 - 60: General Queries
    "kota baje": "⏰ Apnar device-er sthaniyo ghori-ti dekhe nin.",
    "ajker tarikh": "📅 Kaj korar jonno ajker din-ti darun.",
    "abohawa": "🌤️ Sthaniyo abohawar update pete app babohar korun.",
    "khobor": "📰 Sorbosesh khoborer jonno amader news portal dekhun.",
    "bhasa": "🌐 Ami bortomaney Banglish-e kotha bolchi.",
    "version": "💻 Sirocco bot version 2.5 cholche.",
    "ping": "🏓 Pong! System-er response time khubi kom.",
    "server status": "🟢 Shomosto server swabhavik bhabe kaj korche.",
    "admin": "🛡️ Jekono shomosshar jonno prodhan admin-er sathe jogajog korun.",
    "malik": "👑 Eta Sirocco system-er jonno toyri kora hoyeche.",

    # 61 - 70: Action Commands
    "start": "🚀 System safolyo-vabe chalu hoyeche.",
    "stop": "🛑 Automatic process bondho kora hocche.",
    "restart": "🔄 System module-gulo restart kora hocche.",
    "pause": "⏸️ Process samoyik bhabe biroti dewa hoyeche.",
    "resume": "▶️ Karjokrom abar shuru holo.",
    "clear": "🧹 Chat session-er cache porishkar kora hoyeche.",
    "save": "💾 Data safolyo-vabe songrokkhon kora hoyeche.",
    "load": "📂 Kakkhito resource load kora hocche.",
    "delete": "🗑️ System theke item-ti muche fela hoyeche.",
    "verify": "✔️ Jachai-koron prokriya sompurno hoyeche.",

    # 71 - 80: User Assistance
    "pormorsho": "💡 Apnar srijonshil motamotke amra sadubad janai.",
    "অভিযোগ": "⚠️ Apnar shomosshar bistarito amader janan.",
    "review": "⭐ Amader platform-e apnar review din.",
    "rating": "🌟 Amader seba rate korar jonno dhonnobad.",
    "partner": "🤝 Partnership-e agrohi hole jogajog korun.",
    "sponsor": "💼 Sponsorship-er bistarito onurodh sapekkhe dewa hobe.",
    "security": "🔒 Apnar data amader kache sompurno nirapod.",
    "privacy": "🛡️ Amra apnar goponiyo-ta niti bojaye rakhi.",
    "sotto": "📜 Online-e amader babohareer sortaboli pore nin.",
    "policy": "📋 Amader compliance policy update kora hoyeche.",

    # 81 - 90: Extra Casual Responses
    "darun": "😎 Apnar ei kotha-ti darun laglo!",
    "osadharon": "🎉 Bishesher sotti khub bhalo laglo!",
    "chomotkar": "✨ Chomotkar ekti khobor!",
    "thik ache": "👍 Bishoy-ti bujhte perechi.",
    "achha": "👌 Thik ache, bujhechi.",
    "nischoy": "✔️ Obossoi!",
    "sotti": "💯 Ha, ekdom sotti.",
    "hote pare": "🤔 Bhabe dekhi tarpor janacchi.",
    "opekkha koro": "⏳ Doya kore ektu opekkha korun.",
    "prostut": "🚀 Apni prostut thakle shuru kora jak!",

    # 91 - 100: Final Closing Responses
    "bye bye": "👋 Bye bye! Bhalo thakben.",
    "shuvo din": "☀️ Apnar din-ti onek bhalo katuk.",
    "shabdane theko": "🛡️ Nirapode thakun o nijer jotno nin.",
    "shuvokamona": "🍀 Apnar jonno roilo shuvokamona.",
    "abhinondon": "🎉 Apnar safollor jonno abhinondon!",
    "shagotom": "🌟 Apnake ekhane shobshomoy shagotom.",
    "cheers": "🥂 Chomotkar ekti somoyer jonno cheers!",
    "shanti": "🛡️ Apnar mone shanti bojaye thakuk.",
    "somponno": "✅ Kaj-ti safolyo-vabe somponno hoyeche.",
    "sesh": "🏁 Session sesh hoyeche. Biday!"
}

# গান বা মিউজিক সম্পর্কিত নির্দিষ্ট ট্রিগার (কেউ গান চাইলে তবেই রিপ্লাই দেবে)
MUSIC_RESPONSES = {
    "play music": "🎵 Ei nin apnar pochhonder gan-ti bajaacchi! 🎶",
    "song": "🎶 Apnar jonno ekti shundor gan bajano hocche. 🎧",
    "music": "🎧 Music mode chalu hoyeche! Gan-ti upovog korun. 🎼",
    "audio": "🔊 Audio streaming safolyo-vabe shuru hoyeche! 🎵",
    "sing a song": "🎤 Lalalala... Apnar jonno misti shure gan gaicchi! 🎶"
}


def get_banglish_reply(user_text: str) -> str:
    """
    Banglish text input process kore max 1-2 ti emoji sohit uttor dey.
    Nirdishto command chara gan ba music bajabe na.
    """
    clean_text = user_text.strip().lower()
    
    # Prothome check korbe user gan ba music chacche kina
    for music_key, music_response in MUSIC_RESPONSES.items():
        if music_key in clean_text:
            return music_response
            
    # 100 ti nirdishto response check korbe
    for key, response in BANGGLISH_RESPONSES.items():
        if key in clean_text:
            return response
            
    # Match na korle default Banglish reply debe
    return BANGGLISH_RESPONSES["default"]


# Sirocco plugin hisebe register korar function
def load_plugin():
    return {
        "name": "BanglishPlugin",
        "version": "1.0",
        "handler": get_banglish_reply
    }
