import asyncio
import time
from utils.async_file import read_and_print_file_async
from ex1_coroutines import print_after_delay_async


"""
USING GATHER TO RUN COROUTINES CONCURRENTLY
-------------

In the previous exercise the two coroutines `print_after_delay_async`
    and `read_and_print_file_async` were executed synchronously.

This is because they were await-ed one after the other in async_main.
In this exercise you will use `asyncio.gather` to execute them concurrently.

* This file imports `print_after_delay_async(delay, message)` from `ex1_coroutines`.
    Make sure you have implemented this function to sleep for `delay`
    and then print `message`.

* Implement `async_main` to use `asyncio.gather` and run the coroutines
    `print_after_delay_async(1.0, 'Reading file data/users.txt')` and
    `read_and_print_file_async('data/users/txt')` concurrently.

* `asyncio.gather` returns the results (the return values) of all
    coroutines executed. This collection is ordered.

    `read_and_print_file_async` returns the number of lines read from
        the file. Extract this from the return value of
        `asyncio.gather` and modify the print message to
        include the number of lines read.

* Was the message 'Reading file data/users.txt' printed before the file was read?

"""


async def async_main():
    # TODO: Implement async_main to use `asyncio.gather`
    #   to run `print_after_delay_async` and 
    #   `read_and_print_file_async` concurrently
    pass


if __name__ == '__main__':
    start_time = time.time()

    asyncio.run(async_main())

    end_time = time.time()
    print(f'Reading file took {(end_time - start_time):.3f} seconds.')

