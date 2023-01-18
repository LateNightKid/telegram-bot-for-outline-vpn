# Telegram bot for automatic vpn access v1

> **Disclaimer:**
> This project was fully designed and developed by person who is not a professional programmer at all. It probably contains bugs, non-optimal solutions, potential weaknesses, and other joys of entry-level developer's life. In practice, it has shown quite acceptable stability, without dropping at all for almost 8 months of runtime. But use it at your own risk.

## Contents

-   [General description](#description)

-   [Avaliable commands & functional](#avaliable-commands-&-functional)

    -   [Using buttons in bot](#using-buttons-in-bot)
    -   [Using text commands](#using-commands)

-   [How to install & set up](#How-to-install-&-set-up)

    -   [Installing dependencies](#installing-dependencies)
    -   [Configuring](#configuring)
    -   [Adding servers](#adding-servers)
    -   [Bot Start](#bot-start)

-   [Versions](#Versions)

    -   [v1](#v1)
    -   [v2](#v2)

-   [Technical Description](#technical-description)

## General Description

This system was made in order to automate the process of connecting users to the Outline server. Using this Telegram bot, the user can get a key to connect the server without the involvement of server's admin. When user creates a new key, the bot sends an API request to the Outline server and forwards server's answer with the key to a user.

In this system there is also a small separate bot, made for monitoring purpose (further in the text it is called **Monitor Bot**). It notifies the admin that key was created, and sends some details, such as chat id, username, etc. These notifications are intended to keep the admin informed in case of uncontrolled key creation.

## Avaliable commands & functional

### Using buttons

There are two ways for user to communicate with bot. The simplest one is to use buttons.

`New key` button creates a new key for default server and sends it to user. User's telegram @username in that case will be used as a name of the key. For more details about the default server setting, see [adding servers](#adding-servers).

`Help` button sends some short help message. The text can be changed in the `make_help_message` function, which is placed in `message_formatter.py` module.

### Using text commands

There are several text commands for advanced use.

-   `newkey <server_id> <key_name>`, where `server_id` is internal unique id of each server, `key_name` is a string with a custom name of the key. Use `/servers` to see avaliable server ids.
-   `/help` for seeing help message.
-   `/status` for checking the state of a system. With this command, the bot sends an HTTP request to each server, and forwards the HTTP response code to the admin's chat in Monitor Bot.
-   `/servers` shows avaliable servers with its `server_id`, and a short description for each one. See [adding servers](#adding-servers) to know how to change server description.

## How to install & set up

### Installing dependencies

The bots are made with [PyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI), so you need to install it:

```
pip install pyTelegramBotAPI
```

Also, [requests](https://pypi.org/project/requests/) is needed to work with Outline API:

```
pip install requests
```

### Configuring

The script gets bot tokens and Outline API URLs from the environment variables:

-   `OUTLINE_API_URL_0` - The URL for accessing the Management API of your Outline Server. You can find this URL in the Outline Manager Settings tab, or in the output of script you ran to install your Outline Server.
-   `BOT_API_TOKEN` - [API-token](https://core.telegram.org/bots#how-do-i-create-a-bot) of main Telegram bot (that users will work with).
-   `MONITOR_API_TOKEN` - API-token of Monitor Telegram-bot.
-   `ADMIN_CHAT_ID` - A unique id of admin's chat in Monitor Bot. You can find it in `message.chat.id` after sending a message to a Monitor Bot. Monitor Bot will send information about keys created by users to a chat with this id, so be careful with this parameter.

In case you do not want to use environment variables, you then need to set all the variables direclty in `config.py` file. In that file you can also modily the `OUTLINE_DOWNLOAD_LINK` - link for downloading the Client App, that the bot will send to user after creating the key.

### Adding servers

If you have only one Outline server, it is enough to add its API URL to `OUTLINE_API_URL_0` variable.

The bot is able to work with multiple servers. To add more servers, you should modify `servers_description.py` and `config.py` files.
**Each server should has a unique `server_id` integer** inside the bot, and also a short description.
Server with `server_id`= 0 is considered as **default server**. This means that when user clicks on a `New key` button, bot will create a key exactly for that server.

For adding a server, you should append `'server_id':'api_url'` to a `servers` dictionary, and `'server_id':'description string'` to a `servers_description` dictionary.

Here the example of multi-server configuration.

`config.py`:

```python
import os


#Outline API settings
OUTLINE_API_URL_0 = os.getenv('OUTLINE_API_URL_0')   # first server
OUTLINE_API_URL_1 = os.getenv('OUTLINE_API_URL_1')   # second server
OUTLINE_API_URL_2 = os.getenv('OUTLINE_API_URL_2')   # third server
...
```

`servers_description.py`:

```python
from config import OUTLINE_API_URL_0
from config import OUTLINE_API_URL_1
from config import OUTLINE_API_URL_2
...


servers ={
        '0': OUTLINE_API_URL_0,
        '1': OUTLINE_API_URL_1,
        '2': OUTLINE_API_URL_2,
        ...
        }

servers_description = {
        '0': 'Location1',
        '1': 'Location2',
        '2': 'Location3',
        ...
        }
```

### Starting bot

After the setup is complete, run `server.py` to start the bot.

## Versions

### v1

Only Outline management

### v2

in progress

## Tecnical Description
