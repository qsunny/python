import asyncio
import time


start = time.time()


def tic():
    return 'at %1.1f seconds' % (time.time() - start)


async def gr1():
    # Busy waits for a second, but we don't want to stick around...
    print('gr1 started work: {}'.format(tic()))
    # 暂停两秒，但不阻塞时间循环，下同
    await asyncio.sleep(2)
    print('gr1 ended work: {}'.format(tic()))


async def gr2():
    # Busy waits for a second, but we don't want to stick around...
    print('gr2 started work: {}'.format(tic()))
    await asyncio.sleep(2)
    print('gr2 Ended work: {}'.format(tic()))


async def gr3():
    print("Let's do some stuff while the coroutines are blocked, {}".format(tic()))
    await asyncio.sleep(1)
    print("Done!")


if __name__ == '__main__':
    # 事件循环
    ioloop = asyncio.get_event_loop()

    # tasks中也可以使用asyncio.ensure_future(gr1())..
    tasks = [
        ioloop.create_task(gr1()),
        ioloop.create_task(gr2()),
        ioloop.create_task(gr3())
    ]

    ioloop.run_until_complete(asyncio.wait(tasks))
    ioloop.close()