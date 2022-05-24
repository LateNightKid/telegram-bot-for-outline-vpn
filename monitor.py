import telebot
import os


monitor_api_token = os.getenv("MONITOR_API_TOKEN")

monitor = telebot.TeleBot(monitor_api_token)
admin_chat_id = '799341092'

@monitor.message_handler(commands=['start'])
def auth(message):
    global admin_chat_id
    if message.chat.id != admin_chat_id:
        monitor.send_message(message.chat.id, "Denied!")
    print(message)

def new_key_created(key_id,key_name,chat_id,username,firstname,lastname):
    global admin_chat_id
    anwser = "New key created:\n" + "key_id: " + key_id + "\nkey_name: " + key_name + "\nchat_id: " + chat_id + "\nusername: " + username + "\nfirst_name: " + firstname + "\n last_name: " + lastname

    monitor.send_message(admin_chat_id, answer)


monitor.infinity_polling()

