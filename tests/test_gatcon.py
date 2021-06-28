from gatcon import Gatcon
import pytest
from collections.abc import AsyncGenerator


@pytest.fixture
def gatcon():
    return Gatcon()


def test_gatcon_init(gatcon):
    assert isinstance(gatcon, Gatcon)


urls = [f"https://jsonplaceholder.typicode.com/todos/{i+1}" for i in range(10)]


@pytest.mark.asyncio
async def test_gatcon_get_async(gatcon):
    result = await gatcon.get_async(urls[0])
    assert isinstance(result, dict)
    assert result.get("id") == 1


@pytest.mark.asyncio
async def test_gatcon_gather_with_concurrency(gatcon):
    concurrency = 60
    results = await gatcon.gather_with_concurrency(
        concurrency, *[gatcon.get_async(url) for url in urls]
    )
    assert results
    assert isinstance(results, list)
    assert results[8].get("id") == 9


@pytest.mark.asyncio
async def test_gatcon_as_completed_with_concurrency_callback(gatcon):
    concurrency = 60
    await gatcon.as_completed_with_concurrency_callback(
        concurrency,
        print,
        *[gatcon.get_async(url) for url in urls],
    )


@pytest.mark.asyncio
async def test_gatcon_as_completed_with_concurrency(gatcon):
    concurrency = 60
    generator = gatcon.as_completed_with_concurrency(concurrency, *urls)
    assert isinstance(generator, AsyncGenerator)
    async for result in generator:
        assert isinstance(result, dict)
        assert isinstance(result.get("id"), int)
