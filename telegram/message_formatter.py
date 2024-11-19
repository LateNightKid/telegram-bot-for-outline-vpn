from settings import (
    OUTLINE_WINDOWS_DOWNLOAD_LINK,
    OUTLINE_MACOS_DOWNLOAD_LINK,
    OUTLINE_LINUX_DOWNLOAD_LINK,
    OUTLINE_CHOMEOS_DOWNLOAD_LINK,
    OUTLINE_IOS_DOWNLOAD_LINK,
    OUTLINE_ANDROID_DOWNLOAD_LINK,
    OUTLINE_ANDROID_APK_DOWNLOAD_LINK,
    servers_description
    )
from helpers.aliases import ServerId
from textwrap import dedent


def make_message_for_new_key(app: str, access_key: str,
                             server_id: ServerId) -> str:
   #TODO: Add enum class for app.

   if app == "outline":
      message_to_send = dedent(
   f"""Ваш ключ:
      \n<code>{access_key}</code>
      \nНажмите на него, чтобы скопировать.
      \nЛокация сервера: <b>{servers_description.get(server_id)}</b>
      \nЭтот ключ нужно вставить в приложение <b>Outline Client.</b>
      """)

   elif app == "amnezia":
      message_to_send = dedent(
   f"""Ваш ключ:
      \n<code>{access_key}</code>
      \nНажмите на него, чтобы скопировать.
      \nЭтот ключ нужно вставить в приложение <b>Amnezia VPN.</b>
      """)
   else:
      # TODO
      raise Exception

   return message_to_send


def make_download_message() -> str:
    message_to_send = dedent(
    f"""
   <a href="{OUTLINE_WINDOWS_DOWNLOAD_LINK}">Скачать для Windows</a>
   <a href="{OUTLINE_MACOS_DOWNLOAD_LINK}">Скачать для MacOS</a>
   <a href="{OUTLINE_LINUX_DOWNLOAD_LINK}">Скачать для Linux</a>
   <a href="{OUTLINE_CHOMEOS_DOWNLOAD_LINK}">Скачать для ChromeOS</a>
   <a href="{OUTLINE_IOS_DOWNLOAD_LINK}">Скачать для iOS</a>
   <a href="{OUTLINE_ANDROID_DOWNLOAD_LINK}">Скачать для Android</a>
   <a href="{OUTLINE_ANDROID_APK_DOWNLOAD_LINK}">Скачать apk-файл для Android</a>
    """)
    return message_to_send


def make_help_message() -> str:

    message_to_send = "Чтобы создать ключ, нажмите на кнопку. "\
            "\n\nТакже вы можете воспользоваться следующей командой:\n\n"\
            "<code>/newkey server_id key_name</code>\n\n"\
            "<i>server_id</i> - это номер сервера.\n"\
            "<i>key_name</i> - это имя ключа.\n"\
            "Чтобы посмотреть список доступных серверов, введите /servers.\n"\
            "Пример использования команды:\n\n"\
            "<code>/newkey 0 pashahacker</code>\n\n"\


    return message_to_send


def make_servers_list() -> str:

    message_to_send = ""
    for server_id, description in servers_description.items():
        message_to_send += f'server_id: {server_id}, location: {description}\n'
    return message_to_send
