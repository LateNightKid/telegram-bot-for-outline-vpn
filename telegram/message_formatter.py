from settings import (
    OUTLINE_WINDOWS_DOWNLOAD_LINK,
    OUTLINE_MACOS_DOWNLOAD_LINK,
    OUTLINE_LINUX_DOWNLOAD_LINK,
    OUTLINE_CHOMEOS_DOWNLOAD_LINK,
    OUTLINE_IOS_DOWNLOAD_LINK,
    OUTLINE_ANDROID_DOWNLOAD_LINK,
    OUTLINE_ANDROID_APK_DOWNLOAD_LINK,
    servers
    )
from helpers.aliases import ServerId
from textwrap import dedent


def make_message_for_new_key(app: str, access_key: str,
                             server_id: ServerId) -> str:
   if app == "outline":
      message_to_send = dedent(
   f"""Your key:
      \n<code>{access_key}</code>
      \nTap to copy.
      \nServer is located in: <b>{servers[server_id].location}</b>
      \nThis key should be pased in <b>Outline Client.</b>
      """)

   else:
      # TODO
      raise Exception

   return message_to_send


def make_download_message() -> str:
    message_to_send = dedent(
    f"""
   <a href="{OUTLINE_WINDOWS_DOWNLOAD_LINK}">Download for Windows</a>
   <a href="{OUTLINE_MACOS_DOWNLOAD_LINK}">Download for MacOS</a>
   <a href="{OUTLINE_LINUX_DOWNLOAD_LINK}">Download for Linux</a>
   <a href="{OUTLINE_CHOMEOS_DOWNLOAD_LINK}">Download for ChromeOS</a>
   <a href="{OUTLINE_IOS_DOWNLOAD_LINK}">Download for iOS</a>
   <a href="{OUTLINE_ANDROID_DOWNLOAD_LINK}">Download for Android</a>
   <a href="{OUTLINE_ANDROID_APK_DOWNLOAD_LINK}">Download APK</a>
    """)
    return message_to_send


def make_help_message() -> str:

    message_to_send = "Press the button to create a key. "\


    return message_to_send


def make_servers_list() -> str:

    message_to_send = ""
    for server_id, server in servers.items():
        message_to_send += f'server_id: {server_id}, location: {server.location}\n'
    return message_to_send
