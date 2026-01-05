import requests
import threading
import time

def download(url):
    print(f"Starting download from {url}")
    resp = requests.get(url)
    print(f"Finished downloading from {url} and result is {resp.content}")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

threads = []

start = time.time()

for url in urls:
    t = threading.Thread(target=download, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f"All downloads done in {time.time() - start:.2f} seconds")