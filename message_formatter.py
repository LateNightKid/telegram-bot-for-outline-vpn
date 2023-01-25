from config import OUTLINE_DOWNLOAD_LINK, servers_description


def make_message_for_new_key(access_url: str) -> str:

   message_to_send = ("Ваш ключ:\n\n" +
   "<code>" + access_url + "</code>" +
   "\n\nНажмите на него, чтобы скопировать." +
   "\nСкачать Outline Client вы можете по ссылке: " + OUTLINE_DOWNLOAD_LINK)
   return message_to_send


def make_help_message() -> str:

    message_to_send = "Чтобы создать ключ, нажмите на кнопку. "\
            "В этом случае в качестве имени ключа будет указан ваш @username\n"\
            "Если вы хотите ввести другое имя ключа, "\
            "воспользуйтесь следующей командой:\n\n"\
            "<code>newkey server_id key_name</code>\n\n"\
            "<i>server_id</i> - это номер сервера.\n"\
            "<i>key_name</i> - это имя ключа.\n"\
            "Чтобы посмотреть список доступных серверов, введите /servers.\n"\
            "Пример использования команды:\n\n"\
            "<code>newkey 0 pashahacker</code>\n\n"\
            "Если здесь не нашлось ответа на ваш вопрос, свяжитесь с @paveltessman"


    return message_to_send


def make_servers_list() -> str:

    message_to_send = ""
    for server_id, description in servers_description.items():
        message_to_send += f'server_id: {server_id}, location: {description}\n'
    return message_to_send

if __name__ == "__main__":
   print(make_message_for_new_key('test_url'))



