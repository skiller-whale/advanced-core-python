import asyncio
import json
from pathlib import Path
from utils import job_funcs

DATA_PATH = Path(__file__).parent / 'data'

# pylint: disable=pointless-string-statement
"""
In this exercise you will implement a job management service that is
    similar to a cronjob service on UNIX/Linux.

Jobs are specified data/jobs.json as a python function name and a interval in seconds.
{
    "func": "print_date",
    "interval": 2.5
}

Jobs themselves are defined as python function in `jobs` (imported above).

Currently the `__main__` block parses the JSON file into a list of dicts.

1. `main_async` is called with a list of jobs. For each job, schedule
    `_run_job` using `create_task`. Make sure the first argument to `_run_job` is
    a python function (the job) and not its name.

2. Implement `_run_job` to run the job at the interval.

HINT 1: You can use `getattr(jobs, job_name)` to access a python function by its string name.
HINT 2: You can await tasks returned from `create_task`.
"""

async def _run_job(job, interval):
    """Runs `job` asynchronously at an `interval`.

    Args:
        job (func): A function that takes no arguments.
        interval (Numeric): Number of seconds between calls.
    """
    # YOUR CODE GOES HERE
    ...

async def main_async(jobs):
    # YOUR CODE GOES HERE
    ...

if __name__ == '__main__':
    # Read jobs file and parse to a list of dicts
    all_jobs = []

    with open(DATA_PATH / 'jobs.json') as job_file:
        try:
            # Parse JSON file
            contents = json.loads(job_file.read())

            # JSON file should be a list of jobs
            for job_definition in contents:
                all_jobs.append(job_definition)
        except Exception:
            print(f'[error] Error parsing jobs file!')

    # Call main_async to schedule all jobs
    asyncio.run(main_async(all_jobs))
