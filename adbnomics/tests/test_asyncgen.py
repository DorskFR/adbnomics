from ..lib import ConcurAsyncGen
import pytest
from collections.abc import AsyncGenerator


@pytest.fixture
def asyncgen():
    return ConcurAsyncGen()


def test_asyncgen_init(asyncgen):
    assert isinstance(asyncgen, ConcurAsyncGen)


urls = [f"https://jsonplaceholder.typicode.com/todos/{i+1}" for i in range(10)]


@pytest.mark.asyncio
async def test_asyncgen_get_async(asyncgen):
    result = await asyncgen.get_async(urls[0])
    assert isinstance(result, dict)
    assert result.get("id") == 1


@pytest.mark.asyncio
async def test_asyncgen_gather_with_concurrency(asyncgen):
    concurrency = 60
    results = await asyncgen.gather_with_concurrency(
        concurrency, *[asyncgen.get_async(url) for url in urls]
    )
    assert results
    assert isinstance(results, list)
    assert results[8].get("id") == 9


@pytest.mark.asyncio
async def test_asyncgen_as_completed_with_concurrency_callback(asyncgen):
    concurrency = 60
    await asyncgen.as_completed_with_concurrency_callback(
        concurrency,
        print,
        *[asyncgen.get_async(url) for url in urls],
    )


@pytest.mark.asyncio
async def test_asyncgen_as_completed_with_concurrency(asyncgen):
    concurrency = 60
    generator = asyncgen.as_completed_with_concurrency(concurrency, *urls)
    assert isinstance(generator, AsyncGenerator)
    async for result in generator:
        assert isinstance(result, dict)
        assert isinstance(result.get("id"), int)
