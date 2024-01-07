'''Example sync fetch'''
from pprint import pprint
from typing import Any

import requests
from requests import Response


def find_album_by_id(album_id: int) -> dict[str, Any] | None:
    '''A demo func to sync fetch'''
    url = f'https://jsonplaceholder.typicode.com/albums/{album_id}'
    response: Response = requests.get(url, timeout=5000)
    return response.json()['title'] if response.status_code == 200 else None


if __name__ == "__main__":
    pprint(find_album_by_id(1))
