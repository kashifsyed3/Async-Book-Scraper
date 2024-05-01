import requests
import asyncio
import aiohttp
import logging
import async_timeout
import time
from parsers.page_parser import PageParser

logging.basicConfig(level=logging.DEBUG,
                    filename='logs.txt',
                    format='%(asctime)s %(levelname)s %(lineno)d %(message)s')
logger = logging.getLogger('book_scraper')

logger.debug('getting content from html')

books = []
loop = asyncio.get_event_loop()


async def fetch_pages(session, url):
    logger.debug('Getting content from all html pages')
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


page_content = requests.get(f'https://books.toscrape.com').content
page = PageParser(page_content)

urls = [f'https://books.toscrape.com/catalogue/page-{n}.html' for n in range(1, page.total_pages + 1)]

start = time.time()
pages = loop.run_until_complete(getting_multiple_pages(loop, *urls))
end = time.time()
print(f"Loading pages takes {end - start} seconds")

for page_content in pages:
    page = PageParser(page_content)
    books.extend(page.books)
