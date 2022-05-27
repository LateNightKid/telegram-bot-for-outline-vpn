from config import OUTLINE_DOWNLOAD_LINK


def make_message_for_new_key(access_url: str) -> str:

   message_to_send = ("Ваш ключ:\n\n" +
   "<code>" + access_url + "</code>" +
   "\n\nНажмите на него, чтобы скопировать." +
   "\nСкачать Outline Client вы можете по ссылке: " + OUTLINE_DOWNLOAD_LINK)
   return message_to_send

if __name__ == "__main__":
   print(make_message_for_new_key('test_url'))
