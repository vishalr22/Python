'''
Asynchronous I/O is a programming pattern that allows for high-performance I/O operations in a concurrent and non-blocking manner.
In Python, async programming is achieved through the use of the asyncio module and asynchronous functions.

With the asyncio module and asynchronous functions, you can write efficient and scalable code that can handle large amounts of data and I/O operations without blocking the main thread.
'''
import asyncio


async def my_async_function():
    # asynchronous code here
    await asyncio.sleep(1)
    return "Hello, Async World!"


async def main():
    result = await my_async_function()
    print(result)

    # To run Concurrently asyncio.gather is used
    L = await asyncio.gather(
        my_async_function(),
        my_async_function(),
        my_async_function(),
    )
    print(L)

asyncio.run(main())
