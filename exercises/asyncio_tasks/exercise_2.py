import asyncio
import json
from pathlib import Path
from utils.compute_funcs import compute_e, compute_pi

DATA_PATH = Path(__file__).parent / 'data'

# pylint: disable=pointless-string-statement
"""
Similar to exercise_1, this code calculates Euler's number and PI.
Currently it is waiting for both tasks before it stores the results in a file.

This is not good behavior, as if something happens (computer crashes,
    task gets cancelled, etc.), you lose what one function computed.

1. Implement and use the coroutine `process_results(task, results, key)` so that it saves the results
    in `results` and stores them to the file.
"""


def store_results(results, file_path):
    """Stores results as JSON in file_path.

    Args:
        results (dict): Any serializable dictionary.
        file_path (str): Path to file.
    """
    print(f'Storing results in {file_path}.')
    with open(file_path, 'w') as f:
        f.write(json.dumps(results))


async def process_results(task, results, key):
    """Waits for and processes the results of a task

    Args:
        task (asyncio.Task): the task that produces the results.
        results (dict): a reference to a dictionary to store the results of `task` in.
        key (str): they key to `results` to use.
    """
    # TODO: implement
    pass


async def main_async():
    e, pi = await asyncio.gather(
        compute_e(it=50_000),
        compute_pi(it=100_000)
    )

    results = {
        'e': e,
        'pi': pi
    }

    store_results(results, DATA_PATH / 'results.json')


if __name__ == '__main__':
    # Call main_async to schedule all tasks
    asyncio.run(main_async())
