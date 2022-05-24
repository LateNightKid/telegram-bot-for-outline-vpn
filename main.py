import os
import telebot
import py_outline_api
import monitor
from telebot import custom_filters

outline_download_link = 'https://getoutline.org/ru/get-started/'

bot_api_token = os.getenv("BOT_API_TOKEN")

bot = telebot.TeleBot(bot_api_token)

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, """Привет! Этот бот умеет выдавать ключи к прокси-серверу для сотрудников ITGenio.""")


@bot.message_handler(commands = ['status'])
def check_status(message):
    api_status = py_outline_api.check_api_status()
    bot.send_message(message.chat.id, "Bot is online. API status code is {}".format(api_status))


@bot.message_handler(text_startswith = 'newkey')
def make_new_key(message):
    key_name = message.text[7:]
    key = py_outline_api.create_new_key(key_name)

    answer = "Ваш ключ:\n" + key.access_url + "\n" + "Скачать Outline Client вы можете по ссылке: " + outline_download_link
    if key.error_message:
        answer = key.error_message
        monitor.report_error(key.error_message, message.from_user.username, message.from_user.first_name,message.from_user.last_name)

    bot.send_message(message.chat.id, answer)
    monitor.new_key_created(key.id, key.name, message.chat.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)

bot.add_custom_filter(custom_filters.TextStartsFilter())
bot.infinity_polling()
