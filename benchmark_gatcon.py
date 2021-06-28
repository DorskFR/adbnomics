from gatcon import Gatcon
import time
import asyncio

urls = [f"https://jsonplaceholder.typicode.com/todos/{i+1}" for i in range(100)]


async def main():
    gatcon = Gatcon()

    s = time.perf_counter()
    concurrency = 60
    generator = gatcon.as_completed_with_concurrency(concurrency, *urls * 3)
    async for result in generator:
        pass
    elapsed = time.perf_counter() - s
    print(f"Generator: {elapsed}")

    s = time.perf_counter()
    concurrency = 60
    results = await gatcon.gather_with_concurrency(
        concurrency, *[gatcon.get_async(url) for url in urls * 3]
    )
    print(f"Gather: {elapsed}")


if __name__ == "__main__":
    asyncio.run(main())
