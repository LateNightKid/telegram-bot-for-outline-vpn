import telebot
from telebot import types
import monitoring
from outline_api_service import get_new_key
from config import (
        BOT_API_TOKEN,
        DEFAULT_SERVER_ID,
        BLACKLISTED_CHAT_IDS,
        WHITELISTED_CHAT_IDS,
        BLACKLIST,
        WHITELIST
        )
from exceptions import KeyCreationError, KeyRenamingError, InvalidServerIdError
import message_formatter as f
from message_formatter import make_message_for_new_key
from aliases import ServerId
#import pdb

assert BOT_API_TOKEN is not None
bot = telebot.TeleBot(BOT_API_TOKEN, parse_mode='HTML')


def authorize(func):
    def wrapper(message):

        chat_id_to_check = message.chat.id

        if BLACKLIST and str(chat_id_to_check) in BLACKLISTED_CHAT_IDS:
            monitoring.report_blacklist_attempt(message.from_user.username,
                                                chat_id_to_check)
            return

        if WHITELIST and str(chat_id_to_check) not in WHITELISTED_CHAT_IDS:
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
    "Привет! Этот бот для создания ключей Outline VPN.",
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
    if message.text == "Новый ключ":
        server_id = DEFAULT_SERVER_ID
        key_name = _form_key_name(message)
        _make_new_key(message, server_id, key_name)

    elif message.text == "Скачать приложение":
        bot.send_message(message.chat.id,
                         f.make_download_message(),
                         disable_web_page_preview=True
                         )

    elif message.text == "Помощь":
        bot.send_message(message.chat.id, f.make_help_message())

    elif message.text[:7] == "/newkey":
        server_id, key_name = _parse_the_command(message)
        _make_new_key(message, server_id, key_name)

    else:
        bot.send_message(message.chat.id,
                "Команда не распознана.\nИспользуйте /help, чтобы узнать список доступных команд.",
                reply_markup = _make_main_menu_markup())
                

def _make_new_key(message, server_id: ServerId, key_name: str):

    try:
        key = get_new_key(key_name, server_id)
        _send_key(message, key, server_id)

    except KeyCreationError:
        error_message = "API error: cannot create the key"
        _send_error_message(message, error_message)

    except KeyRenamingError:
        error_message = "API error: cannot rename the key"
        _send_error_message(message, error_message)

    except InvalidServerIdError:
        message_to_send = "Сервер с таким ID отсутствует в списке серверов.\n"\
        "Введите /servers, чтобы узнать доступные ID"
        bot.send_message(message.chat.id, message_to_send)


def _send_key(message, key, server_id):

        bot.send_message(
                message.chat.id,
                make_message_for_new_key(key.access_url, server_id)
                )
        monitoring.new_key_created(key.kid, key.name, message.chat.id, 
            server_id)


def _send_error_message(message, error_message):

        bot.send_message(message.chat.id, error_message)

        monitoring.send_error(error_message, message.from_user.username, 
                message.from_user.first_name, message.from_user.last_name)


def _make_main_menu_markup() -> types.ReplyKeyboardMarkup:
    menu_markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    
    keygen_server1_button = types.KeyboardButton("Новый ключ")
    download_button = types.KeyboardButton("Скачать приложение")
    help_button = types.KeyboardButton("Помощь")

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


monitoring.send_start_message()
bot.infinity_polling()
