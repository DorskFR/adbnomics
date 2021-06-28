from adbnomics import ConcurAsyncGen
import time
import asyncio

urls = [f"https://jsonplaceholder.typicode.com/todos/{i+1}" for i in range(100)]


async def main():
    asyncgen = ConcurAsyncGen()

    s = time.perf_counter()
    concurrency = 60
    generator = asyncgen.as_completed_with_concurrency(concurrency, *urls * 3)
    async for result in generator:
        pass
    elapsed = time.perf_counter() - s
    print(f"Generator: {elapsed}")

    s = time.perf_counter()
    concurrency = 60
    results = await asyncgen.gather_with_concurrency(
        concurrency, *[asyncgen.get_async(url) for url in urls * 3]
    )
    print(f"Gather: {elapsed}")


if __name__ == "__main__":
    asyncio.run(main())
