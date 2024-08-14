import os


#Outline api servers settings
OUTLINE_API_URL_0 = os.getenv('OUTLINE_API_URL_0')

servers ={                          # {'server_id':'api_url'}
        '0': OUTLINE_API_URL_0
        }


servers_description = {             # {'server_id' : 'description'}
        '0': 'Амстердам'
        }


#Main bot settings
BOT_API_TOKEN = os.getenv("BOT_API_TOKEN")
DEFAULT_SERVER_ID = "0"


#Message formatter settings
OUTLINE_DOWNLOAD_LINK = 'https://getoutline.org/ru/get-started/#step-3'
ADMIN_USERNAME_IN_HELP_MESSAGE = os.getenv('ADMIN_USERNAME_IN_HELP_MESSAGE')


#Monitoring bot settings
MONITOR_API_TOKEN = os.getenv("MONITOR_API_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")


BLOCKED_CHAT_IDS = [ 

        ]


