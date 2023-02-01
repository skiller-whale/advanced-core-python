import asyncio
import time
from utils.async_file import read_and_print_file_sync, read_and_print_file_async

"""
COROUTINES
-------------

Currently, this script uses only synchronous functions. Your task is to convert it so
    that it uses coroutines (async functions).

The module utils.async_file provides two functions for reading (and printing) a file
    line-by-line. `read_and_print_file_sync` is synchronous and 
    `read_and_print_file_async` -- asynchronous (a coroutine).
    You do not need to understand the details of how they are implemented for this task.

Both functions simulate reading a file with a delay when opening, reading individual
    lines and closing -- this simulates a slow filesystem.

* Run the script. How long does it take to run?

* Create a coroutine (asynchronous function) called main_async that does nothing.
    (You can use `pass` just like in a regular function).

* Modify the `if __name__ == '__main__'` block so that it uses
    `asyncio.run` to run the `main_async` coroutine.

    NOTE: Don't modify the runtime computation code (you'll need this later).

* Inside `main_async`, use `read_and_print_file_async` to read
    and print the file `data/users.txt` line by line.
    `read_and_print_file_async` has the same signature as 
    `read_and_print_file_sync` -- it takes one argument (the file name).

* Similar to `main_sync`, store and print the number of lines read
    at the end of `read_and_print_file_async` in `main_async`.

* Create a function called `print_after_delay_async(delay, message)`.
    This should behave like `print_after_delay_sync` without using
    `time.sleep` and instead using an appropriate call to
    a method from the `asyncio` module.

* Execute the coroutine `print_after_delay_async` to print the message
    'Reading file data/users.txt' after a 1 second delay at the
    start of `main_async` (similarly to `main_sync`).

* How long does it take to run the async version of the script?
"""


def print_after_delay_sync(delay, message):
    """Prints a message after a delay (synchronous)

    Args:
        delay (float): Delay (in seconds) to sleep for.
        message (str): Message to print.
    """
    time.sleep(delay)
    print(message)

def main_sync():
    """Synchronous main function.
    """
    print_after_delay_sync(1.0, 'Reading file data/users.txt')
    lines_read = read_and_print_file_sync('data/users.txt')
    print(f'Done, read {lines_read} lines!')

# TODO: Create and implement the coroutine async_main

# TODO: Create and implement the coroutine print_after_delay_async

if __name__ == '__main__':
    # NOTE: Do not remove timing computation
    start_time = time.time()

    ## TODO: Run async_main using asyncio.run instead
    main_sync()

    end_time = time.time()
    print(f'Reading file took {(end_time - start_time):.3f} seconds.')

