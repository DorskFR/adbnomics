import asyncio
import aiohttp


class Gatcon:
    def __init__(self):
        pass

    async def gather_with_concurrency(self, n, *tasks):
        semaphore = asyncio.Semaphore(n)

        async def sem_task(task):
            async with semaphore:
                return await task

        return await asyncio.gather(*(sem_task(task) for task in tasks))

    async def as_completed_with_concurrency_callback(self, n, callback, *tasks):
        semaphore = asyncio.Semaphore(n)

        async def sem_task(task):
            async with semaphore:
                return await task

        for coro in asyncio.as_completed([sem_task(task) for task in tasks]):
            result = await coro
            callback(result)

    async def as_completed_with_concurrency(self, n, *urls):
        semaphore = asyncio.Semaphore(n)

        async def sem_task(url):
            async with semaphore:
                return await self.get_async(url)

        for coro in asyncio.as_completed([sem_task(url) for url in urls]):
            yield await coro

    async def get_async(self, url):
        conn = aiohttp.TCPConnector(limit=None, ttl_dns_cache=300)
        async with aiohttp.ClientSession(connector=conn) as session:
            response = await session.get(url, ssl=False)
            return await response.json()
