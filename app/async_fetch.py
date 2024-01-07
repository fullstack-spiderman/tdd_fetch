'''Example async fetch'''
import asyncio
from pprint import pprint
from typing import Any
from urllib.parse import urljoin

from httpx import AsyncClient, Response


async def fetch_api(endpoint: str) -> Response:
    base_url: str = 'https://jsonplaceholder.typicode.com'
    url: str = urljoin(base_url, endpoint)

    async with AsyncClient() as session:
        response: Response = await session.get(url)
        return response


async def async_find_album_by_id(album_id: int) -> Response:
    '''A demo func to sync fetch'''
    endpoint: str = f"/albums/{album_id}"
    response: Response = await fetch_api(endpoint)
    return response


if __name__ == "__main__":
    response: Response = asyncio.run(async_find_album_by_id(1))
    response.raise_for_status()
    data: dict[str, Any] | None = response.json()
    pprint({"data": data})
