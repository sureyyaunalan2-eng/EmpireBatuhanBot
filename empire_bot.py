from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "8693336963:AAHrZQzXBkr3nwtuBn5eIFWaQRs8JaRvFJY"


# 🕐 SAATLİK MESAJ
# Burayı sen daha sonra dolduracaksın.
# 🕐 SAATLİK MESAJ
HOURLY_MESSAGE = """🦋 WEB SİTEMİZ ⚡️⬇️⬇️
GÜVENLE OYNAYABİLECEĞİNİZ SİTELER:
⚡️ https://ebatuhan.com

🔜 YOUTUBE KANALIMIZ:
📱 https://www.youtube.com/@ebatuhan

𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 𝐆𝐑𝐔𝐏𝐋𝐀𝐑𝐈𝐌𝐈𝐙 ⚡️

⚡️ SOHBET: https://t.me/ebatuhan
⚡️ DUYURU: https://t.me/ebatuhanduyuru"""


# 🦋 Yeni üye
async def new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🦋 Empire Batuhan ailesine hoş geldiniz!\n"
        "💬 Sohbetimize katılmayı ve keyifli vakit geçirmeyi unutmayın."
    )


# 🤖 /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hoş geldin!\n"
        "Empire Batuhan grubuna hoş geldin."
    )


# 📖 /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 Yardım\n\n"
        "Destek için grup yöneticileriyle iletişime geçebilirsiniz."
    )


# 💬 Otomatik cevaplar
async def automatic_reply(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    # 👋 MERHABA / SELAM
    if "merhaba" in text or "selam" in text:
        await update.message.reply_text(
            "🦋 Merhaba! Hoş geldin."
        )

    # 🌐 SITE / LINK
    elif "site" in text or "link" in text:
        await update.message.reply_text(
            "🌐 Güncel site bağlantımıza buradan ulaşabilirsiniz:\n"
            "https://ebatuhan.com"
        )

    # 📩 DESTEK
    elif "destek" in text:
        await update.message.reply_text(
            "📩 Destek için yetkililerle iletişime geçebilirsiniz.\n"
            "@empirebatuhanmod"
        )

    # 📱 TELEGRAM
    elif "telegram" in text:
        await update.message.reply_text(
            "📱 Telegram gruplarımız:\n"
            "Sohbet: https://t.me/ebatuhan"
        )

    # ▶️ YOUTUBE
    elif "youtube" in text:
        await update.message.reply_text(
            "▶️ YouTube kanalımız:\n"
            "https://www.youtube.com/@ebatuhan"
        )

    # 📢 DUYURU
    elif "duyuru" in text:
        await update.message.reply_text(
            "📢 Duyuru kanalımız:\n"
            "https://t.me/ebatuhanduyuru"
        )

    # 🎁 BONUS / KAMPANYA
    elif "bonus" in text or "kampanya" in text:
        await update.message.reply_text(
            "🎁 Güncel kampanya bilgileri için:\n"
            "https://ebatuhan.com"
        )


# 🕐 Saatlik görev
async def hourly_message(context: ContextTypes.DEFAULT_TYPE):

    # Geçici test grubunun ID'si
    GROUP_ID = -5446725698

    # Mesaj boşsa hiçbir şey gönderme
    if not HOURLY_MESSAGE:
        return

    await context.bot.send_message(
        chat_id=GROUP_ID,
        text=HOURLY_MESSAGE
    )


# 🚀 BOTU BAŞLAT
def main():

    app = (
    Application.builder()
    .token(TOKEN)
    .connect_timeout(60)
    .read_timeout(60)
    .write_timeout(60)
    .pool_timeout(60)
    .get_updates_connect_timeout(60)
    .get_updates_read_timeout(60)
    .get_updates_write_timeout(60)
    .get_updates_pool_timeout(60)
    .build()
)

    # /start
    app.add_handler(
        CommandHandler("start", start)
    )

    # /help
    app.add_handler(
        CommandHandler("help", help_command)
    )

    # 🦋 Yeni üye geldiğinde
    app.add_handler(
        MessageHandler(
            filters.StatusUpdate.NEW_CHAT_MEMBERS,
            new_member
        )
    )

    # 💬 Normal mesajlara otomatik cevap
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            automatic_reply
        )
    )

    # 🕐 Her 1 saatte bir
    app.job_queue.run_repeating(
        hourly_message,
        interval=3600,
        first=3600
    )

    print("🤖 Empire Batuhan bot çalışıyor!")

    app.run_polling()


if __name__ == "__main__":
    main()