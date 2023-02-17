# -*- codiing:utf-8 -*-
"""
测试你的 Internet 速度
pip install google
"""

__author__ = "aaron.qiu"

from pprint import pprint
import asyncio
import httpx
import threading
import time

def sync_main(url, sign):
    response = httpx.get(url).status_code
    print(f'sync_main: {threading.current_thread()}: {sign}: {response}')


client = httpx.AsyncClient()


async def async_main(url, sign):
    response = await client.get(url)
    status_code = response.status_code
    print(f'async_main: {threading.current_thread()}: {sign}:{status_code}')


if __name__ == "__main__":
    # sync_start = time.time()
    # [sync_main(url='http://www.baidu.com', sign=i) for i in range(200)]
    # sync_end = time.time()
    # print(sync_end - sync_start)

    loop = asyncio.get_event_loop()
    tasks = [async_main(url='http://www.baidu.com', sign=i) for i in range(200)]
    async_start = time.time()
    loop.run_until_complete(asyncio.wait(tasks))
    async_end = time.time()
    loop.close()
    print(async_end - async_start)

