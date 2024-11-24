from helpers.classes import OutlineServer
import json


JSON_FILENAME = "devsettings.json"

with open(JSON_FILENAME, 'r') as file:
    settings = json.load(file)

_tg_settings = settings['tg_bot_settings']
_outline_dl_links = settings['outline_dl_links']


BOT_API_TOKEN = _tg_settings['main_bot_api_token']
MONITOR_API_TOKEN = _tg_settings['monitor_bot_api_token']

ADMIN_CHAT_ID = _tg_settings['admin_chat_id']

DEFAULT_SERVER_ID = _tg_settings['default_server_id']

ENABLE_BLACKLIST = _tg_settings['enable_blacklist']
ENABLE_WHITELIST = _tg_settings['enable_whitelist']

BLACKLISTED_CHAT_IDS = _tg_settings['blacklisted_chat_ids']
WHITELISTED_CHAT_IDS = _tg_settings['whitelisted_chat_ids']

OUTLINE_WINDOWS_DOWNLOAD_LINK = _outline_dl_links['windows']
OUTLINE_MACOS_DOWNLOAD_LINK = _outline_dl_links['macos']
OUTLINE_LINUX_DOWNLOAD_LINK = _outline_dl_links['linux']
OUTLINE_CHOMEOS_DOWNLOAD_LINK = _outline_dl_links['chromeos']
OUTLINE_IOS_DOWNLOAD_LINK = _outline_dl_links['android']
OUTLINE_ANDROID_DOWNLOAD_LINK = _outline_dl_links['android']
OUTLINE_ANDROID_APK_DOWNLOAD_LINK = _outline_dl_links['apk']


def _read_outline_servers_from_settings() -> dict[str, OutlineServer]:

    servers = {}
    for server in settings['outline_servers']:
        if server['is_enabled']:
            id = server['id']
            srv = OutlineServer(
                    api_url=server.get('api_url'),
                    location=server.get('location'),
                    is_enabled=True)

            servers[id] = srv
    return servers
                

servers = _read_outline_servers_from_settings()
