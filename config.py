import os


#Outline api settings
OUTLINE_API_URL_0 = os.getenv('OUTLINE_API_URL_0')

#Main bot settings
BOT_API_TOKEN = os.getenv("BOT_API_TOKEN")

#Message formatter settings
OUTLINE_DOWNLOAD_LINK = 'https://getoutline.org/ru/get-started/'

#Monitoring bot settings
MONITOR_API_TOKEN = os.getenv("MONITOR_API_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")
STATUS_CHECK_FREQUENCY = 60*30 #this value should be in seconds. Now it's one message per 30 mins

