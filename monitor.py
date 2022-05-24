import telebot
import os


monitor_api_token = os.getenv("MONITOR_API_TOKEN")

monitor = telebot.TeleBot(monitor_api_token)
admin_chat_id = '799341092'

#@monitor.message_handler(commands=['start'])
#def auth(message):
#    global admin_chat_id
#    if message.chat.id != admin_chat_id:
#        monitor.send_message(message.chat.id, "Denied!")
#    print(message)

def new_key_created(key_id,key_name,chat_id,username,firstname,lastname):
    global admin_chat_id
    answer = "New key created:\n" + "key_id: " + str(key_id) + "\nkey_name: " + str(key_name) + "\nchat_id: " + str(chat_id) + "\nusername: " + str(username) + "\nfirst_name: " + str(firstname) + "\n last_name: " + str(lastname)

    monitor.send_message(admin_chat_id, answer)

def report_error(error_message, username, firstname, lastname):
    answer = "Error detected!" + "\nerror_message: " + str(error_message) + "\nuser_name" + str(username) + "\nfirst_name" + str(firstname) + "\nlast_name" + str(lastname)
    monitor.send_message(admin_chat_id, answer)


#monitor.infinity_polling()

