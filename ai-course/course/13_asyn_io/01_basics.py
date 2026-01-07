import asyncio

async def main():
    print("Hello, World!")
    await asyncio.sleep(2)
    print("World, Hello completed!")

asyncio.run(main())