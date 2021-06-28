import asyncio
from gatcon import Gatcon
from cleaner import Cleaner
from saver import Saver
from toc import TOC


def make_url(provider, dataset, indicator):
    base_url = "https://api.db.nomics.world/v22/series/"
    params = "?observations=true&metadata=false&format=json&limit=1000&offset=0"
    return f"{base_url}{provider}/{dataset}/A..{indicator}{params}"


def make_urls():
    urls = [make_url("IMF", k, v) for row in TOC for k, v in row.items()]
    return urls


async def process_result(result):
    if result.get("message") and "not found" in result.get("message"):
        return
    cleaner = Cleaner(result)
    saver = Saver(cleaner.result)
    saver.to_csv("output")


async def main():
    gatcon = Gatcon()
    urls = make_urls()[0:100]
    concurrency = 60
    generator = gatcon.as_completed_with_concurrency(concurrency, *urls)
    async for result in generator:
        await process_result(result)


if __name__ == "__main__":
    asyncio.run(main())


# async def download_toc():
#     response_json = await gatcon.get_async(url)


# toc
# while True:
# fetch list of datasets
# append(result)
# if found > limit + offset
# offset += limit
# iterate over toc and build list of URLS
