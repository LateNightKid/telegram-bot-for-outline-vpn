import telebot
from telebot import types
from settings import (
        BOT_API_TOKEN,
        DEFAULT_SERVER_ID,
        BLACKLISTED_CHAT_IDS,
        WHITELISTED_CHAT_IDS,
        ENABLE_BLACKLIST,
        ENABLE_WHITELIST
        )
import telegram.monitoring as monitoring
import outline.api as outline
from settings import BOT_API_TOKEN, DEFAULT_SERVER_ID, BLACKLISTED_CHAT_IDS
from helpers.exceptions import KeyCreationError, KeyRenamingError, InvalidServerIdError
import telegram.message_formatter as f
from helpers.aliases import ServerId


assert BOT_API_TOKEN is not None
bot = telebot.TeleBot(BOT_API_TOKEN, parse_mode='HTML')


def authorize(func):
    def wrapper(message):

        chat_id_to_check = message.chat.id

        if ENABLE_BLACKLIST and str(chat_id_to_check) in BLACKLISTED_CHAT_IDS:
            monitoring.report_blacklist_attempt(message.from_user.username,
                                                chat_id_to_check)
            return

        if ENABLE_WHITELIST and str(chat_id_to_check) not in WHITELISTED_CHAT_IDS:
            monitoring.report_not_in_whitelist(message.from_user.username,
                                                chat_id_to_check)
            return

        return func(message)
    return wrapper


@bot.message_handler(commands = ['status'])
@authorize
def send_status(message):
    monitoring.send_api_status()


@bot.message_handler(commands = ['start'])
@authorize
def send_welcome(message):
    bot.send_message(message.chat.id,
    "Hey! This bot is used for creating Outline keys.",
    reply_markup = _make_main_menu_markup())

    
@bot.message_handler(commands = ['help'])
@authorize
def send_help(message):
    bot.send_message(message.chat.id, f.make_help_message())


@bot.message_handler(commands = ['servers'])
@authorize
def send_servers_list(message):
    bot.send_message(message.chat.id, f.make_servers_list())


@bot.message_handler(content_types = ['text'])
@authorize
def anwser(message):
    if message.text == "New Outline Key":
        server_id = DEFAULT_SERVER_ID
        key_name = _form_key_name(message)
        _make_new_key(message, server_id, key_name)

    elif message.text == "Download Outline":
        bot.send_message(message.chat.id,
                         f.make_download_message(),
                         disable_web_page_preview=True
                         )

    elif message.text == "Help":
        bot.send_message(message.chat.id, f.make_help_message())

    elif message.text[:7] == "/newkey":
        server_id, key_name = _parse_the_command(message)
        _make_new_key(message, server_id, key_name)

    else:
        bot.send_message(message.chat.id,
                "Unknown command.",
                reply_markup = _make_main_menu_markup())
                

def _make_new_key(message, server_id: ServerId, key_name: str):

    try:
        key = outline.get_new_key(key_name, server_id)

        _send_key(message, key, server_id)

    except KeyCreationError:
        error_message = "API error: cannot create the key"
        _send_error_message(message, error_message)

    except KeyRenamingError:
        error_message = "API error: cannot rename the key"
        _send_error_message(message, error_message)

    except InvalidServerIdError:
        message_to_send = "The server id does not exist."
        bot.send_message(message.chat.id, message_to_send)


def _send_key(message, key, server_id):

    text = f.make_message_for_new_key("outline", key.access_url, server_id)

    bot.send_message(
            message.chat.id,
            text
            )
    monitoring.new_key_created(key.kid, key.name, message.chat.id, 
        server_id)


def _send_error_message(message, error_message):

        bot.send_message(message.chat.id, error_message)

        monitoring.send_error(error_message, message.from_user.username, 
                message.from_user.first_name, message.from_user.last_name)


def _make_main_menu_markup() -> types.ReplyKeyboardMarkup:
    menu_markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    
    keygen_server1_button = types.KeyboardButton("New Outline Key")
    download_button = types.KeyboardButton("Download Outline")
    help_button = types.KeyboardButton("Help")

    menu_markup.add(
            keygen_server1_button,
            download_button,
            help_button
            )
    return menu_markup


def _parse_the_command(message) -> list:
    arguments = message.text[8:].split()

    if arguments != []:
        server_id = arguments[0]
    else:
        server_id = DEFAULT_SERVER_ID

    key_name = ''.join(arguments[1:])

    if key_name == '': 
        key_name = _form_key_name(message)
    
    return [server_id, key_name]


def _form_key_name(message) -> str:
    key_name = message.from_user.username

    return key_name


def start_telegram_server():
    monitoring.send_start_message()
    bot.infinity_polling()
