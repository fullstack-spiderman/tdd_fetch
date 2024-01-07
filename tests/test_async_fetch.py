'''test module for test_async_find_album_by_id'''
from typing import Any

import pytest
from pytest_httpx import HTTPXMock

from app.async_fetch import async_find_album_by_id


pytestmark: pytest.MarkDecorator = pytest.mark.anyio


async def test_async_find_album_by_id(httpx_mock: HTTPXMock) -> None:
    '''test code for test_async_find_album_by_id'''
    httpx_mock.add_response(
        method="GET",
        url='https://jsonplaceholder.typicode.com/albums/1', json={
            "userId": 1,
            "id": 1,
            "title": "enim"
        })

    result: dict[str, Any] | None = await async_find_album_by_id(1)
    assert result == 'enim'
