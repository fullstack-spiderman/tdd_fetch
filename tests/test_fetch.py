'''test module for test_find_album_by_id'''
from typing import Any

from requests_mock.mocker import Mocker

from app.fetch import find_album_by_id


def test_find_album_by_id(requests_mock: Mocker) -> None:
    '''test code for test_find_album_by_id'''
    requests_mock.get(
        url='https://jsonplaceholder.typicode.com/albums/1', json={
            "userId": 1,
            "id": 1,
            "title": "enim"
        })
    result: dict[str, Any] | None = find_album_by_id(1)
    assert result == 'enim'
