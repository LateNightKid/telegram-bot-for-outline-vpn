# Telegram bot for creating OutlineVPN keys.

> **Disclaimer:**
> This project was fully designed and developed by person who is not a professional programmer at all. It probably contains bugs, non-optimal solutions, potential weaknesses, and other joys of entry-level developer's life. In practice, it has shown quite acceptable stability, without dropping at all for more of 12 months of runtime. But use it at your own risk.

## Contents

-   [Known issues](#known-issues)
-   [General description](#general-description)
-   [Commands and features](#comands-and-features)
    -   [Using buttons](#using-buttons)
    -   [Using text commands](#using-text-commands)
-   [How to install & set up](#How-to-install-&-set-up)
    -   [Installing dependencies](#installing-dependencies)
    -   [Configuring](#configuring)
    -   [Adding servers](#adding-servers)
    -   [Starting the bot](#starting-the-bot)


## Known issues

If Outline server is down, the bot freezes for a minute after sending any request, until the timeout exception is thrown ``¯\_( ͡° ͜ʖ ͡°)_/¯`` Asynchronous calls to be made in the future.

## General Description

This system was made in order to automate the process of connecting users to the Outline server. Using this Telegram bot, a user can get a key and connect to the server without involvement of a server's admin. When the user creates a new key, the bot sends an API request to the Outline server and forwards server's answer with the key to the user.

In this system there is also a small separate bot (yeah, the second one), made for monitoring purpose (further in the text it is called **Monitor Bot**). It notifies the admin that a key was created, and sends some details, such as chat id, username, etc. These notifications are intended to keep the admin informed in case of uncontrolled key creation.

## Commands and features

### Using buttons

There are two ways for user to communicate with the bot. The simplest one is to use buttons.

`New key` button creates a new key for the default server and sends it to the user. User's @username in that case will be used as a name of the key. For more details about the default server settings, see [adding servers](#adding-servers).

`Help` button sends some short help message. The message text can be changed in the `make_help_message` function, which is placed in `message_formatter.py`.

### Using text commands

There are several text commands for advanced use.

-   `/newkey <server_id> <key_name>`, where `server_id` is an internal unique id of each server, `key_name` is a string with a name of the key. 
-   `/help` to get help message.
-   `/status` for checking the status of the system. With this command, the bot sends an HTTP request to each server, and forwards the HTTP response code to the admin's chat in Monitor Bot.
-   `/servers` shows available servers with its `server_id`, and a short description for each one. 

## How to install & set up

### Installing dependencies

The bots are made with [PyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI), so you need to install it:

```
pip install pyTelegramBotAPI
```

Also, [requests](https://pypi.org/project/requests/) is used to work with Outline API:

```
pip install requests
```

### Configuring

The script gets bot tokens and Outline API URLs from the following environment variables:

-   `OUTLINE_API_URL_0` - the URL which is used to access the Management API of your Outline Server. You can find this URL in the Outline Manager Settings tab, or in the output of script you ran while installing your Outline Server.
-   `BOT_API_TOKEN` - the [API-token](https://core.telegram.org/bots#how-do-i-create-a-bot) of main Telegram bot (that users will work with).
-   `MONITOR_API_TOKEN` - API-token of Monitor Telegram-bot. Can be the same as the main bot's token. In that case, all the monitoring messages will be sent in the admin's chat of the main bot.
-   `ADMIN_CHAT_ID` - A unique id of admin's chat in Monitor Bot. You can find out your chat id by running `get_admin_chat_id.py` script. 

In case you do not want to use environment variables, you then need to set all the variables directly in `config.py` file. In that file you can also modify the `OUTLINE_DOWNLOAD_LINK` - link for downloading the Client App, that the bot will send to user after creating the key.

### Adding servers

If you have only one Outline server, it is enough to add its API URL to `OUTLINE_API_URL_0` variable. No other action is required.

The bot is able to work with multiple servers. To add more servers, you should modify  `config.py` file.

**Each server should has a unique `server_id` number** inside the bot, and also a short description. The id and description of each server are shown after the `/servers` command.
Server with `server_id` = 0 is considered as **default server**. That means, when the user clicks on the `New key` button, the bot will create a key for server whose `server_id` is 0.

To add a server, you should:
1. Append `'server_id':'api_url'` to the `servers` dictionary.
2. Append `'server_id':'description string'` to the `servers_description` dictionary.

Here is the example of multi-server configuration.

`config.py`:

```python
import os


#Outline API settings
OUTLINE_API_URL_0 = os.getenv('OUTLINE_API_URL_0')   # first server
OUTLINE_API_URL_1 = os.getenv('OUTLINE_API_URL_1')   # second server
OUTLINE_API_URL_2 = os.getenv('OUTLINE_API_URL_2')   # third server

servers ={
        '0': OUTLINE_API_URL_0,                      # {'server_id':'api_url'}
        '1': OUTLINE_API_URL_1,
        '2': OUTLINE_API_URL_2,
        ...
        }

servers_description = {
        '0': 'Location1',                             # {'server_id' : 'description'}
        '1': 'Location2',
        '2': 'Location3',
        ...
        }
```

### Starting the bot

After the setup is complete, run `server.py` to start the bot.


