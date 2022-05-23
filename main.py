import os
import telebot
import py_outline_api
from telebot import custom_filters

outline_download_link = 'https://getoutline.org/ru/get-started/'

bot_api_token = os.getenv("BOT_API_TOKEN")

bot = telebot.TeleBot(bot_api_token)

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, """Привет! Этот бот умеет выдавать ключи к прокси-серверу для сотрудников ITGenio.""")


@bot.message_handler(commands = ['help'])
def send_help(message):
    bot.send_message(message.chat.id, """""")


@bot.message_handler(text_startswith = 'newkey')
def make_new_key(message):
    user_name = message.text[7:]
    key = py_outline_api.create_new_key(user_name)

    answer = "Ваш ключ:\n" + key + "\n" + "Скачать Outline Client вы можете по ссылке: " + outline_download_link
    bot.send_message(message.chat.id, answer)

bot.add_custom_filter(custom_filters.TextStartsFilter())
bot.infinity_polling()
