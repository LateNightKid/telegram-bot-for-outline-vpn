import telebot
from telebot import types
import monitoring
from outline_api_service import get_new_key
from config import BOT_API_TOKEN
from exceptions import KeyCreationError, KeyRenamingError, InvalidServerIdError
from message_formatter import make_message_for_new_key
from aliases import ServerId


bot = telebot.TeleBot(BOT_API_TOKEN, parse_mode='HTML')
menu_markup = types.ReplyKeyboardMarkup(resize_keyboard = True)


@bot.message_handler(commands = ['status'])
def send_status(message):
    monitoring.send_api_status()



@bot.message_handler(commands = ['start'])
def send_welcome(message):
    _make_main_menu_markup()
    bot.send_message(message.chat.id,
    "Привет! Этот бот умеет выдавать ключи к прокси-серверу для сотрудников ITGenio.",
    reply_markup = menu_markup)


@bot.message_handler(content_types = ['text'])
def anwser(message):
    if message.text == "Новый ключ":
        server_id = "0"
        key_name = _form_key_name(message)
        _make_new_key(message, server_id, key_name)

    elif message.text[:6] == "newkey ":
        server_id, key_name = _parse_the_command(message)
        _make_new_key(message, server_id, key_name)

    else:
        bot.send_message(message.chat_id, "Unknown syntax!")


def _make_new_key(message, server_id: ServerId, key_name: str):

    try:
        key = get_new_key(key_name, server_id)
        _send_key(message, key)

    except KeyCreationError:
        error_message = "API error: cannot create the key"
        _send_error_message(message, error_message)

    except KeyRenamingError:
        error_message = "API error: cannot rename the key"
        _send_error_message(message, error_message)

    except InvalidServerIdError:
        error_message = "Invalid server ID"
        _send_error_message(message, error_message)


def _send_key(message, key):

        bot.send_message(
                message.chat.id,
                make_message_for_new_key(key.access_url)
                )
        monitoring.new_key_created(key.kid, key.name, message.chat.id, 
            message.from_user.username, message.from_user.first_name, 
            message.from_user.last_name)


def _send_error_message(message, error_message):

        bot.send_message(message.chat.id, error_message)

        monitoring.send_error(error_message, message.from_user.username, 
                message.from_user.first_name, message.from_user.last_name)


def _make_main_menu_markup():
    global menu_markup
    
    keygen_server1_button = types.KeyboardButton("Новый ключ")
    menu_markup.add(keygen_server1_button)

def _parse_the_command(message) -> list:
    arguments = message.text[7:].split()
    server_id = arguments[0]
    try:
        key_name = ''.join(arguments[1:])
    except IndexError:
        key_name = _form_key_name(message)

    
    return [server_id, key_name]

def _form_key_name(message) -> str:

    return message.from_user.username


monitoring.send_start_message()
monitoring.send_api_status()
bot.infinity_polling()
