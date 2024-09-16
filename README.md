# Telegram bot for creating OutlineVPN keys.

## Contents

-   [Known issues](#known-issues)
-   [General description](#general-description)
-   [Features overview](#features-overview)
    -   [Using buttons](#using-buttons)
    -   [Using text commands](#using-text-commands)
-   [How to install & set up](#How-to-install-&-set-up)
    -   [Installing dependencies](#installing-dependencies)
    -   [Configuring](#configuring)
    -   [Adding servers](#adding-servers)
    -   [Starting the bot](#starting-the-bot)


## Known issues

If Outline server is down, the bot hangs up for a minute after sending a request, until the timeout exception is thrown ``¯\_( ͡° ͜ʖ ͡°)_/¯`` Asynchronous calls to be made in the future.

## General Description

Suppose, you're an admin of one or more Outine VPN servers. And suppose, you want to share keys with users, but don't want to be bothered by them every time they need a key.
This project will help you. With this Telegram bot, a user can obtain a server key without your participation.

This project consists of a Telegram bot which for interacting woth users, Outline API module for creating keys and a small monitoring bot for you to be aware of when somebody creates a key. When the user obtains a new key, the bot sends an API request to the Outline server, gets a new key and forwards the key to the user. At the same time you get a message from a monitoring bot that a new key has been created.

## Features overview

### Using buttons

There are two ways for the user to communicate with the bot. The simplest one is to use buttons.

`New key` button creates a new key for the default server. User's @username in that case will be used as a name of the key. 

`Download Outline` button to get a list of download links for different devices.

`Help` button sends some short help message. You can change the message text in the `make_help_message` function, which is placed in `message_formatter.py`.

### Using text commands

There are several text commands for advanced use.

-   `/newkey <server_id> <key_name>`, where `server_id` is an internal unique id of each server, `key_name` is a string with the name for the key. 
-   `/help` to get help message.
-   `/status` to check if the servers are up. With this command, the bot sends an HTTP request to each server, and forwards the HTTP response code to the admin's chat in Monitor Bot.
-   `/servers` to show available servers with its `server_id`, and a short description for each one. 

## How to install & set up

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

### Configuring

To understand how the configuration works, let's consider a basic example when you have only one Oultline server.

Set the following environment variables:

-   `OUTLINE_API_URL_0` - the URL to access the Management API of your Outline Server. You can find that URL in the Outline Manager Settings tab, or in the output of the script you ran when installing your Outline Server.
-   `BOT_API_TOKEN` - the [API-token](https://core.telegram.org/bots#how-do-i-create-a-bot) of the main Telegram bot (that users will interact with).
-   `MONITOR_API_TOKEN` - the API-token of the Telegram-bot that will be sending notifications to you. If equals to `BOT_API_TOKEN`, then all the monitoring messages will be sent in the admin's chat of the main bot.
-   `ADMIN_CHAT_ID` - A unique id of the admin's chat in Monitor Bot. To find out your chat id, run `get_admin_chat_id.py` script. It will tell you what to do.

In case you do not want to use environment variables, you can set all the variables directly in `config.py` file. In that file you can also modify the download links that bot will be sending to users.

Also, you should look at `servers_description` in the `config.py` and change the description for your server. This is the description that users will see when creating a key or listing available servers. I personally prefer specifying server's location.

That's all for one-server-configuration. After you've done all the steps, run `server.py` to start the bot.

### Adding servers

The bot is able to work with multiple servers. To add more servers, you should modify  `config.py` file:

1. Append `'server_id':'api_url'` to the `servers` dictionary.
2. Append `'server_id':'description string'` to the `servers_description` dictionary.

Yeap, that's pretty lame to have two dictionaries here, I know... I hope I will be able to change the design soon.

Server with `server_id` = 0 is considered as **default server**. That means, when the user clicks on the `New key` button, the bot will create a key for server whose `server_id` is 0.

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
