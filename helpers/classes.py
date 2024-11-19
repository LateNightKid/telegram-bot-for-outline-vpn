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
