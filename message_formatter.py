from config import OUTLINE_DOWNLOAD_LINK, servers_description
from aliases import ServerId


def make_message_for_new_key(access_url: str, server_id: ServerId) -> str:

   message_to_send = ("Ваш ключ:\n\n" +
   "<code>" + access_url + "</code>" +
   "\n\nНажмите на него, чтобы скопировать." +
   "\n\nЛокация сервера: " + "<b>" + servers_description.get(server_id) + "</b>" +
   "\n\nСкачать Outline Client вы можете по ссылке: " + OUTLINE_DOWNLOAD_LINK)
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

if __name__ == "__main__":
   print(make_message_for_new_key('test_url'))
