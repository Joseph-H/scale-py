import asyncio

"""
Asyncio is centered on the concept of event loops. An event loop is when something waits for something to be done.
Once those things are done then execution can continue

"""


async def add_42(number):
    """This is a coroutine"""
    print("Adding 42")
    return 42 + number


async def hello_world_plus():
    print("hello world!")
    # you can call a coroutine from another coroutine
    result = await add_42(23)
    return result

hello_world_coroutine = hello_world_plus()
print(hello_world_coroutine)  # <coroutine object hello_world at 0x10a709b90>

event_loop = asyncio.get_event_loop()
print("entering event loop")
result = event_loop.run_until_complete(hello_world_coroutine)
print(result)

# another example below


async def hello_world():
    print("hello world!")


async def hello_python():
    print("hello Python!")
    # this is the async implementation of time.sleep
    await asyncio.sleep(0.1)

event_loop = asyncio.get_event_loop()
try:
    # gather allows you to wait for several coroutines to finish
    result = event_loop.run_until_complete(asyncio.gather(
        hello_world(),
        hello_python(),
    ))
    print(result)
finally:
    event_loop.close()
