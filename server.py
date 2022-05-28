import telebot
import monitoring
from threading import Thread
from outline_api_service import get_new_key
from telebot import custom_filters
from config import BOT_API_TOKEN
from exceptions import KeyCreationError, KeyRenamingError
from message_formatter import make_message_for_new_key


bot = telebot.TeleBot(BOT_API_TOKEN, parse_mode='HTML')

@bot.message_handler(commands = ['status'])
def send_status(message):
    monitoring.send_api_status()



@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
    "Привет! Этот бот умеет выдавать ключи к прокси-серверу для сотрудников ITGenio.")


@bot.message_handler(text_startswith = 'newkey')
def make_new_key(message):
    key_name = message.text[7:]
    try:
        key = get_new_key(key_name)

        bot.send_message(
                message.chat.id,
                make_message_for_new_key(key.access_url)
                )
        monitoring.new_key_created(key.kid, key.name, message.chat.id, 
            message.from_user.username, message.from_user.first_name, 
            message.from_user.last_name)

    except KeyCreationError:
        error_message = "API error: cannot create the key"
        bot.send_message(message.chat.id, error_message)

        monitoring.send_error(error_message, message.from_user.username, 
                message.from_user.first_name, message.from_user.last_name)

    except KeyRenamingError:
        error_message = "API error: cannot rename the key"
        bot.send_message(message.chat.id, error_message)

        monitoring.send_error(error_message, message.from_user.username, 
                message.from_user.first_name, message.from_user.last_name)

status_checking_tread = Thread(target=monitoring.send_api_status)
status_checking_tread.start()
bot.add_custom_filter(custom_filters.TextStartsFilter())
bot.infinity_polling()
