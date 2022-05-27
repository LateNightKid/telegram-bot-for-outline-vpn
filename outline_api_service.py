import requests
import json
from typing import NamedTuple
from config import OUTLINE_API_URL
from exceptions import KeyCreationError, KeyRenamingError


AccessUrl = str
KeyId = str
StatusCode = str


class Key(NamedTuple):
    kid: KeyId
    name: str
    access_url: AccessUrl


def get_new_key(key_name: str) -> Key:
    api_response = _create_new_key() 
    key_id = api_response.get('id')
    access_url = api_response.get('accessUrl')

    _rename_key(key_id, key_name)
    key = Key(kid=key_id, name=key_name, access_url=access_url)

    return key

    
def check_api_status() -> StatusCode:
    url = OUTLINE_API_URL + '/access-keys'
    r = requests.get(url, verify=False)
    return str(r.status_code)


def _create_new_key() -> dict:
    request_url = OUTLINE_API_URL + '/access-keys'
    r = requests.post(request_url, verify=False)    

    if int(r.status_code) > 299:
        raise KeyCreationError
    
    return _parse_response(r)


def _parse_response(response: requests.models.Response) -> dict:
    return json.loads(response.text)


def _rename_key(key_id: KeyId, key_name: str) -> None:
    rename_url = OUTLINE_API_URL + '/access-keys/' + key_id + '/name'
    r = requests.put(rename_url, data = {'name': key_name}, verify=False)  

    if int(r.status_code) > 299:
        raise KeyRenamingError
