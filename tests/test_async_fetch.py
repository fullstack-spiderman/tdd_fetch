'''test module for test_async_find_album_by_id'''
import pytest
from pytest_httpx import HTTPXMock
from httpx import Response

from app.async_fetch import (
    async_find_album_by_id,
    async_find_all_albums,
    async_find_all_posts,
    async_find_post_by_id,
)

pytestmark: list[pytest.MarkDecorator] = [
    pytest.mark.asyncio,
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
        url='https://jsonplaceholder.typicode.com/albums/', json=mocked_response
    )

    response: Response = await async_find_all_albums()

    assert response.status_code == 200
    assert response.json() == mocked_response


@pytest.mark.smoke
async def test_async_find_post_by_id(httpx_mock: HTTPXMock) -> None:
    '''test code for async_find_post_by_id'''
    post_id: int = 100
    mocked_response: dict[str, int|str] = {
            "userId": post_id,
            "id": post_id,
            "title": f"sample post{post_id} title",
            "body": f"sample post body{post_id}"
        }
    httpx_mock.add_response(
        method="GET",
        url=f'https://jsonplaceholder.typicode.com/posts/{post_id}', json=mocked_response,
    )

    response: Response = await async_find_post_by_id(post_id)

    assert response.status_code == 200
    assert response.json() == mocked_response


async def test_async_find_all_posts(httpx_mock: HTTPXMock) -> None:
    '''test code for async_find_all_posts'''
    mocked_response: list[dict[str, int|str]] = [
        {
            "userId": 1,
            "id": 1,
            "title": "sample post1 title",
            "body": "sample post body1"
        },
         {
            "userId": 5,
            "id": 5,
            "title": "sample post5 title",
            "body": "sample post body5"
        }
    ]
    httpx_mock.add_response(
        method="GET",
        url='https://jsonplaceholder.typicode.com/posts/', json=mocked_response
    )

    response: Response = await async_find_all_posts()

    assert response.status_code == 200
    assert response.json() == mocked_response