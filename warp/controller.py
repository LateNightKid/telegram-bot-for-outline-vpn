import subprocess
from helpers.classes import AmneziaKey


def get_new_key(key_name: str | None, server_id: str) -> AmneziaKey:

    if key_name == None:
        key_name = server_id

    key_base64 = _generate_warp_key_base64()
    key = AmneziaKey(name=key_name, access_url=key_base64)

    return key


def _generate_warp_key_base64():
        output = subprocess.run("warp/generate_warp_config.sh",
                                capture_output=True,
                                text=True
                                )
        return output.stdout
