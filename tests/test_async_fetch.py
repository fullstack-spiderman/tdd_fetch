'''test module for test_async_find_album_by_id'''
from typing import Any
from httpx import Response

import pytest
from pytest_httpx import HTTPXMock

from app.async_fetch import async_find_album_by_id

pytestmark: list[pytest.MarkDecorator] = [
    pytest.mark.asyncio,
    pytest.mark.smoke,
]

async def test_async_find_album_by_id(httpx_mock: HTTPXMock) -> None:
    '''test code for async_find_album_by_id'''

    mocked_response: dict[str, int|str] = {
            "userId": 2,
            "id": 2,
            "title": "spiderman"
        }
    httpx_mock.add_response(
        method="GET",
        url='https://jsonplaceholder.typicode.com/albums/1', json=mocked_response,
    )

    response: Response = await async_find_album_by_id(1)

    assert response.status_code == 200
    assert response.json() == mocked_response

async def test_async_find_all_albums(httpx_mock: HTTPXMock) -> None:
    '''test code for async_find_all_albums'''
    mocked_response: list[dict[str, int|str]] = [
        {
            "userId": 1,
            "id": 1,
            "title": "ironman"
        },
        {
            "userId": 2,
            "id": 2,
            "title": "spiderman"
        }
    ]
    httpx_mock.add_response(
        method="GET",
        url='https://jsonplaceholder.typicode.com/albums/', json=mocked_response)

    response: dict[str, Any] | None = await async_find_all_albums()

    assert response.status_code == 200
    assert response.json() == mocked_response