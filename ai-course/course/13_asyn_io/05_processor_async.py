import asyncio
from concurrent.futures import ProcessPoolExecutor

def encypt(data):
    return f"🔒 {data[::-1]} is encrypted now";

async def main():
    loop = asyncio.get_running_loop();
    with ProcessPoolExecutor() as pool:
        res = await loop.run_in_executor(pool, encypt, "secret_data_needs_to_be_encrypted");
        print(res)


if __name__ == "__main__":
    asyncio.run(main())
