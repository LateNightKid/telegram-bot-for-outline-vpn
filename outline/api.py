import requests
import json
from urllib3.exceptions import InsecureRequestWarning
from helpers.aliases import AccessUrl, KeyId, ServerId
from helpers.classes import OutlineKey
from helpers.exceptions import KeyCreationError, KeyRenamingError, InvalidServerIdError
from settings import servers


def get_new_key(key_name: str | None, server_id: ServerId) -> OutlineKey:

    if servers.get(server_id) == None:
        raise InvalidServerIdError

    api_response = _create_new_key(server_id) 

    key_id = api_response['id']

    access_url = api_response['accessUrl']
    if key_name == None:
        key_name = "key_id:" + key_id

    _rename_key(key_id, key_name, server_id)

    assert key_name is not None
    key = OutlineKey(kid=key_id, name=key_name, access_url=access_url)

    return key

    
def check_api_status() -> dict:
    global servers
    _disable_ssl_warnings()
    api_status_codes = {}
    for server_id, server in servers.items():
        url = server.api_url + '/access-keys'
        r = requests.get(url, verify=False)
        api_status_codes.update({server_id: str(r.status_code)})
    return api_status_codes


def _create_new_key(server_id: ServerId) -> dict:
    request_url = servers[server_id].api_url + '/access-keys'
    r = requests.post(request_url, verify=False)    

    if int(r.status_code) != 201:
        raise KeyCreationError
    
    return _parse_response(r)


def _parse_response(response: requests.models.Response) -> dict:
    return json.loads(response.text)


def _rename_key(key_id: KeyId, key_name: str | None, server_id: ServerId) -> None:
    rename_url = servers[server_id].api_url + '/access-keys/' + key_id + '/name'
    r = requests.put(rename_url, data = {'name': key_name}, verify=False)  
    if int(r.status_code) != 204: 
        raise KeyRenamingError


def _disable_ssl_warnings():
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":
    check_api_status()
