import telebot
import time
from outline_api_service import check_api_status
from config import MONITOR_API_TOKEN, ADMIN_CHAT_ID


monitor = telebot.TeleBot(MONITOR_API_TOKEN)

def new_key_created(key_id: int, key_name: str, chat_id: int, username: str,
        firstname: str, lastname: str) -> None:
    answer = ("New key created:" + 
            "\nkey_id: "     + str(key_id) + 
            "\nkey_name: "   + str(key_name) + 
            "\nchat_id: "    + str(chat_id) + 
            "\nusername: "   + str(username) + 
            "\nfirst_name: " + str(firstname) + 
            "\n last_name: " + str(lastname))

    monitor.send_message(ADMIN_CHAT_ID, answer)


def send_error(error_message: str, username: str, firstname: str,
        lastname: str) -> None:

    answer = ("Error detected!" + 
            "\nerror_message: " + error_message + 
            "\nuser_name: "     + username + 
            "\nfirst_name: "    + firstname + 
            "\nlast_name: "     + lastname)

    monitor.send_message(ADMIN_CHAT_ID, answer)

def send_api_status():
    while True:
        api_status_code = check_api_status() 

        monitor.send_message(ADMIN_CHAT_ID, f"API status code: {api_status_code}")
        time.sleep(60*60*30)    # one status message per 30 mins
