import requests
import os
import json

api_url = os.getenv('API_URL')

def create_new_key():
    url = api_url + '/access-keys'
    r = requests.post(url, verify=False)    # Creating a new key

    response = json.loads(r.text)
    key_id = responce.get('id')
    
    rename_url = api_url + '/access-keys/' + key_id + '/name'
    r = requests.put(remane_url, data = {'name': user_name}, verify=False)  # Renaming the key
    return key_id

    
