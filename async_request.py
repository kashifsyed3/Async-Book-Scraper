import asyncio
import aiohttp
import async_timeout

loop = asyncio.get_event_loop()
urls = [f'https://google.com' for n in range(50)]


async def fetch_pages(session, url):
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()


async def getting_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_pages(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks

pages = loop.run_until_complete(getting_multiple_pages(loop, *urls))
