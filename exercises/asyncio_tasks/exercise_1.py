import asyncio
import time
from pathlib import Path
from utils.compute_funcs import compute_e, compute_pi

DATA_PATH = Path(__file__).parent / 'data'

# pylint: disable=pointless-string-statement
"""
This code calculates Euler's number (e) and PI. Currently it is waiting for `pi`
    to compute before starting to compute `e`.

1. Convert the `coroutine` calls to use `asyncio.create_task` and print results as they are available.

N.B.: You don't need to understand or edit the code that computes e or pi.
"""

async def main_async():
    pi = await compute_pi(it=100_000)
    e = await compute_e(it=50_000)

if __name__ == '__main__':
    t_start = time.time()

    # Call main_async to schedule all tasks
    asyncio.run(main_async())

    print(f'Execution time: {time.time() - t_start:.3}s')
