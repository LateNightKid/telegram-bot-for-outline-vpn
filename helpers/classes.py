from typing import NamedTuple
from helpers.aliases import AccessUrl, KeyId, ServerId


class Key(NamedTuple):
    pass


class OutlineKey(NamedTuple):
    kid: KeyId
    name: str
    access_url: AccessUrl


class AmneziaKey(NamedTuple):
    name: str
    access_url: str


class OutlineServer:
    def __init__(self, api_url: str,
                  location: str, is_enabled: bool) -> None:
        self.api_url = api_url
        self.location = location
        self.is_enabled = is_enabled
