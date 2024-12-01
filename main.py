import logging
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Defaults
from telegram import ReplyKeyboardMarkup

# Config
from config import BOT_TOKEN

# Message_handler
from message import message_handler


# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# set logging httpx
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Json data
with open("./static_texts.json", 'r', encoding='utf-8') as file:
    static_texts = json.load(file)

# Main start handler
def start(update, context):

    user = update.effective_user

    update.message.reply_text(text=static_texts['startText1'].format(user.full_name), parse_mode='HTML')

    # Show bot commands
    context.bot.set_my_commands([
        ("start", "Botni ishga tushurish"),
        ("help", "Yordam"),
    ])


# For the help button
def help_command(update, context):
    # Button
    keyboard = [
        ["👨‍💻 Yaratuvchi"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(text=static_texts['helpText'], reply_markup=reply_markup, parse_mode='HTML')


def main():
    defaults = Defaults(timeout=10)

    updater = Updater(token=BOT_TOKEN, use_context=True, defaults=defaults)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(MessageHandler(Filters.text, message_handler))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

