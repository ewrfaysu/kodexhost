import telebot

# ================= CONFIG =================
BOT_TOKEN = "8980253607:AAEAJ-rwLcG41EhSrFxtph51af8OJAMwsZs"

bot = telebot.TeleBot(BOT_TOKEN)


# ================= /START =================
@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "🤖 Bot is working!\n\n"
        f"👤 Your id: {message.from_user.id}\n"
        "✅ Support: @kodexofc"
    )


# ================= /HELP =================
@bot.message_handler(commands=["help"])
def help_command(message):
    bot.reply_to(
        message,
        "📚 Comman:\n"
        "/start - Bot start\n"
        "/help - Show help\n\n"
    )


# ================= TEXT REPLY =================
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(
        message,
        f"{message.text}"
    )


# ================= RUN =================
print("🤖 Bot is running...")
print("Press CTRL+C to stop.")

bot.infinity_polling()