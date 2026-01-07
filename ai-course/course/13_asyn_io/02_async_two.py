import asyncio
import time

async def brew(name):
    print(f"Brewing {name} chai...")
    await asyncio.sleep(3)
    print(f"All Done {name}")

async def main():
    print(f"Main running")
    start = time.time()
    await asyncio.gather(brew("Masala"), brew("Macha"))
    print(f"Main completed")
    print(f"Completion took {time.time() - start:.2f}")

async def main2():
    print(f"Main running")
    start = time.time()
    await brew("Masala")
    await brew("Macha")
    print(f"Main completed")
    print(f"Completion took {time.time() - start:.2f}")

asyncio.run(main2())
