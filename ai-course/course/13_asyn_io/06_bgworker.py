import asyncio
import threading
import time
import os

def back_worker():
    while True:
        time.sleep(1)
        print(f"Logging system health 🖥");


async def fetch_order():
    await asyncio.sleep(3)
    print("Log from order fetched")


threading.Thread(target=back_worker, daemon=True).start();

asyncio.run(fetch_order())

