import asyncio


@asyncio.coroutine
def fact(name, num):
    f = 1
    for i in range(2, num+1):
        print("%s: Compute factorial(%s)..." % (name, i))
        yield from asyncio.sleep(1)
        f *= i
    print("%s: factorial(%s) = %s" % (name, num, f))


loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(fact("A", 2)),
    asyncio.ensure_future(fact("B", 3)),
    asyncio.ensure_future(fact("C", 4))
    ]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()