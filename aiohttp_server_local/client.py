import aiohttp
import asyncio


FILE = "client.html"
data = {'4': 'Hello',
        '5': 'World'}


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost:8080/post', data=data) as response:
            return await response.text()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

