import requests
import os
import json
from key import Key
from requests.packages.urllib3.exceptions import InsecureRequestWarning

api_url = os.getenv('API_URL')

def create_new_key(key_name):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    url = api_url + '/access-keys'
    error_message = ''
    r = requests.post(url, verify=False)    # Creating a new key
    if int(r.status_code) > 399:
        error_message = "Что-то пошло не так, позовите Администратора.\nНе получилось создать ключ. Статус запроса: " + r.status_code
        return response

    response = json.loads(r.text)
    key_id = response.get('id')
    access_url = response.get('accessUrl')
    
    rename_url = api_url + '/access-keys/' + key_id + '/name'
    r = requests.put(rename_url, data = {'name': key_name}, verify=False)  # Renaming the key

    if int(r.status_code) > 399:
        error_message = "Ключ создан, но не получилось его переименовать. Статус запроса: " + r.status_code

    key = Key(key_id,key_name,access_url, error_message)
    return key

    
def check_api_status():
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    url = api_url + '/access-keys'
    r = requests.get(url, verify=False)
    status_code = r.status_code
    return status_code
