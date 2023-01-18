import telebot
import random


print('Enter monitor bot API token')

monitor_bot_token = input()

bot = telebot.TeleBot(monitor_bot_token)

check_code = random.randint(100000,999999)

print('Send this code to bot:\n', check_code)

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    if message.text == str(check_code):
        print('\nThe code has been recieved from:', message.from_user.username)
        print('Your admin chat id:\n', message.chat.id)
        print('\nHit Ctrl+C to exit')


bot.infinity_polling()
