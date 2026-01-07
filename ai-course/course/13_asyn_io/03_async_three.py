import asyncio
import aiohttp
import time

async def getFromRemote(session, url):
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}");

async def main():
    urls = ["https://httpbin.org/delay/5"] * 4
    async with aiohttp.ClientSession() as session:
        tasks = [getFromRemote(session, url) for url in urls]
        await asyncio.gather(*tasks)

start = time.time();

asyncio.run(main())

print(f"Task complition took {time.time() - start:.2F}")