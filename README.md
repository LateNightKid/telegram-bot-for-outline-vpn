# Telegram bot for creating OutlineVPN keys.

## Contents

-   [Known issues](#known-issues)
-   [General description](#general-description)
-   [Features overview](#features-overview)
-   [How to install](#how-to-install)
    -   [Installing dependencies](#installing-dependencies)
    -   [Download the bot](#download-the-bot)
-   [How to configure](#how-to-configure)
    -   [Configuring servers](#configuring-servers)
    -   [Bot settings](#bot-settings)
    -   [Download links](#download-links)
    -   [Example configuration](#example-configuration)
-   [How to run](#how-to-run)
-   [How to use](#how-to-use)
    -   [Buttons](#buttons)
    -   [Text commands](#text-commands)


## Known issues

If Outline server is down, the bot hangs up for a minute after sending a request, until the timeout exception is thrown ``¯\_( ͡° ͜ʖ ͡°)_/¯`` Asynchronous calls to be made in the future.

## General Description

Suppose, you're an admin of one or more Outine VPN servers. And suppose, you want to share keys with users, but don't want to be bothered by them every time they need a key.
This project will help you. With this Telegram bot, a user can obtain a server key without your participation.

This project consists of a Telegram bot which for interacting with users, Outline API module for creating keys and a small monitoring bot for you to be aware of when somebody creates a key. When the user obtains a new key, the bot sends an API request to the Outline server, gets a new key and forwards the key to the user. At the same time you get a message from a monitoring bot that a new key has been created.

## How to install

### Installing dependencies

This project works on Python 3.10 and newer.
The bot is made with [PyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI), so you need to install it:

```
pip install pyTelegramBotAPI
```

Also, [requests](https://pypi.org/project/requests/) is used to work with Outline API:

```
pip install requests
```

### Download the bot

Next, time to download the bot itself:

```
cd ~
git clone https://github.com/LateNightKid/telegram-bot-for-outline-vpn.git 
cd telegram-bot-for-outline-vpn
```

## How to configure

Do you see the `settings.json` file? Yeap, this is the file where all configuration will take place.

### Configuring servers

The first field in the file is `outline_servers`. This is how the bot knows how to talk with your outline servers and create keys.

- `id` is a unique internal id of the server. It can be any string, but it should be unique for each server. 
- `api_url` is the outline management api that you got when installing outline on the server. Looks something like `https://123.123.123.123:65536/XXXXXXXXXXXX_XXXXXXXXX`. You can also find it in the Outline Manager app (take a look at server settings page there).
- `location` a place where the server is located. This will be shown to users when a key is created.
- `is_enabled` - boolean value. If false, the server will not be added into the bot.

### Bot settings

Next, let's configure the bot itself.

- `main_bot_api_token` is a token for your telegram bot.
- `monitor_api-token` is a token for your secondary bot, where you will be seeing monitoring messages.
Could be the same as the main bot, or separate.
- `admin_chat_id` is the id of the chat where monitoring messages will go. To find out your chat id, run `utils/get_admin_chat_id.py` and follow the instructions.
- `default_server_id` - if you have several servers, which one will be used when a user press the Create Key button? Set its id here.
- `enable_blacklist` - Set to True, if you want to enable the blacklist feature.
- `enable_whitelist` - Set to True, if you want to enable the whitelist feature.
- `blacklisted_chat_ids` - Enumerate all the chat ids that should not have access to the bot. Do not forget to set `enable_blacklist` to True.
- `whilelisted_chat_ids` - Only the users with chat ids listed here will have access to the bot, if `enable_whitelist` is set to True.

### Download links

The last section of the json is download links  that will be shown to users. You can chaange it as you wish.

### Example configuration

At this point, the `settings.json` file should look something like this:

```json
{
    "outline_servers": [
        {
            "id": "server1",
            "api_url": "https://123.123.123.123:65536/XXXXXXXXXXXX_XXXXXXXXX",
            "location": "Somewhere",
            "is_enabled": true
        },
        {
            "id": "server2",
            "api_url": "https://456.456.456.456:65536/XXXXXXXXXXXX_XXXXXXXXX",
            "location": "Somewhere else",
            "is_enabled": true
        }
    ],

    "tg_bot_settings": 
        {
            "main_bot_api_token": "<your-tg-token-goes-here>",
            "monitor_bot_api_token": "<your-tg-token-goes-here>",

            "admin_chat_id": "123456789",

            "default_server_id": "server1",

            "enable_blacklist": true,
            "enable_whitelist": false,

            "blacklisted_chat_ids": ["987654321", "543219876"],
            "whitelisted_chat_ids": []
        },

    "outline_dl_links":
        {
            "windows" : "https://s3.amazonaws.com/outline-releases/client/windows/stable/Outline-Client.exe",
            "macos"   : "https://itunes.apple.com/us/app/outline-app/id1356178125",
            "linux"   : "https://s3.amazonaws.com/outline-releases/client/linux/stable/Outline-Client.AppImage",
            "chromeos": "https://play.google.com/store/apps/details?id=org.outline.android.client",
            "ios"     : "https://itunes.apple.com/us/app/outline-app/id1356177741",
            "android" : "https://play.google.com/store/apps/details?id=org.outline.android.client",
            "apk"     : "https://s3.amazonaws.com/outline-releases/client/android/stable/Outline-Client.apk"
        }
}

```

## How to run

When configured, run it with:

```
python3 run.py
```

## How to use

### Buttons

There are two ways for the user to communicate with the bot. The simplest one is to use buttons.

`New key` button creates a new key for the default server. User's @username in that case will be used as a name of the key. 

`Download Outline` button to get a list of download links for different devices.

`Help` button sends some short help message. You can change the message text in the `make_help_message` function, which is placed in `message_formatter.py`.

### Text commands

There are several text commands for advanced use.

-   `/newkey <server_id> <key_name>`, where `server_id` is an internal unique id of each server, `key_name` is a string with the name for the key. 
-   `/help` to get help message.
-   `/status` to check if the servers are up. With this command, the bot sends an HTTP request to each server, and forwards the HTTP response code to the admin's chat in Monitor Bot.
-   `/servers` to show available servers with its `server_id`, and a short description for each one. 


