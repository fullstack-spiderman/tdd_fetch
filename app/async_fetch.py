'''Example async fetch'''
import asyncio
from pprint import pprint
from typing import Any

import httpx


async def async_find_album_by_id(album_id: int) -> dict[str, Any] | None:
    '''A demo func to sync fetch'''
    url = f'https://jsonplaceholder.typicode.com/albums/{album_id}'
    async with httpx.AsyncClient() as session:
        response = await session.get(url)
        return response.json()["title"] if response.status_code == 200 else None


if __name__ == "__main__":
    result: dict[str, Any] | None = asyncio.run(async_find_album_by_id(1))
    pprint(result)
