import requests
import os
import json

api_url = os.getenv('API_URL')

def create_new_key():
    url = api_url + '/access-keys'
    r = requests.post(url, verify=False)    # Creating a new key
    if int(r.status_code) > 399:
        response = "Что-то пошло не так, позовите Администратора.\nНе получилось создать ключ. Статус запроса: " + r.status_code
        return response

    response = json.loads(r.text)
    key_id = responce.get('id')
    
    rename_url = api_url + '/access-keys/' + key_id + '/name'
    r = requests.put(remane_url, data = {'name': user_name}, verify=False)  # Renaming the key
    if int(r.status_code) > 399:
        error_message = "Ключ создан, но не получилось его переименовать. Статус запроса: " + r.status_code + "Попробуйте воспользоваться ключом, возможно, он все же работает: "
        return (error_message + key_id)
    return key_id

    
